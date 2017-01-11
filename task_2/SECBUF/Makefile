BIN=secbuf
CC=gcc
CFLAGS=-z execstack -m32 -static -g -ggdb -O0 -fno-stack-protector 
USER=SECBUF

$(BIN):
	$(CC) $(CFLAGS) -o $(BIN) $(BIN).c
	sudo chown $(USER):$(USER) $(BIN)
	sudo chmod u+s $(BIN)

.PHONY: clean $(BIN)

clean:
	rm -f $(BIN)
