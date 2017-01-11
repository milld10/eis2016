#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>

#define BUFFER_SIZE 1024
#define on_error(...) { fprintf(stderr, __VA_ARGS__); fflush(stderr); exit(1); }

typedef struct {
  char* content;
  size_t* size;
  int client_fd;
} Data;

int load_file(char* fname, int fnsize, char** filebuffer, size_t* filesize);
void* serve_file(void* param);

int main ()
{
  int port = 1337;
  int server_fd, client_fd, err;
  struct sockaddr_in server, client;
  char buf[BUFFER_SIZE];
  char* filebuffer = NULL;
  size_t filesize = 0;
  pthread_t serve_thread;
  Data info;

  server_fd = socket(AF_INET, SOCK_STREAM, 0);
  if (server_fd < 0)
    on_error("Could not create socket\n");

  server.sin_family = AF_INET;
  server.sin_port = htons(port);
  server.sin_addr.s_addr = htonl(INADDR_ANY);

  int opt_val = 1;
  setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt_val, sizeof opt_val);
  err = bind(server_fd, (struct sockaddr *) &server, sizeof(server));
  if (err < 0)
    on_error("Could not bind socket\n");

  err = listen(server_fd, 128);
  if (err < 0)
    on_error("Could not listen on socket\n");

  printf("Server is listening on %d\n", port);

  while (1)
  {
    socklen_t client_len = sizeof(client);
    client_fd = accept(server_fd, (struct sockaddr *) &client, &client_len);

    if (client_fd < 0)
      on_error("Could not establish new connection\n");

    while (1)
    {
      char* server_elo = "What file can I serve you?\n";
      err = send(client_fd, server_elo, strlen(server_elo)+1, 0);
      if (err < 0)
        on_error("Client write failed\n");

      int read = recv(client_fd, buf, BUFFER_SIZE, 0);
      if (!read)
        break; // done reading
      if (read < 0)
        on_error("Client read failed\n");

      err = load_file(buf, read, &filebuffer, &filesize);
      if(err < 0)
      {
        char* msg = "tried to fool me?\n";
        err = send(client_fd, msg, strlen(msg), 0);
        if (err < 0)
        {
          on_error("Client write failed\n");
        }
      }
      else
      {
        info.content = filebuffer;
        info.size = &filesize;
        info.client_fd = client_fd;
        pthread_create(&serve_thread, NULL, serve_file, &info);
      }
    }
  }
  return 0;
}

int load_file(char* fname, int fnsize, char** filebuffer, size_t* filesize)
{
  fname[fnsize - 1] = '\0';
  if(access(fname, F_OK) == -1)
  {
    fclose(fopen(fname, "wb"));
    return -1;
  }
  
  FILE *f = fopen(fname, "rb");
  fseek(f, 0, SEEK_END);
  *filesize = ftell(f);
  fseek(f, 0, SEEK_SET); 

  *filebuffer = malloc(*filesize + 1);
  fread(*filebuffer, *filesize, 1, f);
  fclose(f);
  (*filebuffer)[*filesize] = 0;
  if(!((*filebuffer)[0] == 'O' && \
       (*filebuffer)[1] == 'g' && \
       (*filebuffer)[2] == 'g'))
    return -1;
  return 0;
}

void* serve_file(void* param)
{ 
  Data info = *(Data*)param;
  if(!info.content)
    return NULL;
  int err = send(info.client_fd, info.content, *(info.size), 0);
  if (err < 0)
    on_error("Client write failed\n");
}
