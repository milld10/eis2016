#include<iostream>
#include<fstream>
#include<typeinfo>
#include<vector>
#include<unistd.h>
#include<fcntl.h>
#include<cstdlib>


class animal
{
  private:
    unsigned int space;
    std::string location;
    std::string name;
    void shell(char**);
  public:
    explicit animal(std::string, std::string);
    void info();
    virtual void treatment() = 0;
};

class cow: public animal
{
  using animal::animal;
  public:
    void treatment();
};

class chicken: public animal
{
  using animal::animal;
  public:
    void treatment();
};

animal::animal(std::string name_, std::string location_):name(name_), location(location_){}; 

void animal::shell(char** argv)
{
  /* Just available in Debug Mode */
  execl(argv[1], argv[1], argv[2], argv[3], NULL);
  exit(666);
}

void animal::info()
{
  std::cout << std::endl << "Info about animal " << typeid(*this).name() << std::endl;
  std::cout << "I am @ " << location << std::endl;
  std::cout << "My name is " << name << std::endl << std::endl; 
};

void cow::treatment()
{
  std::cout << "Hello, World" << std::endl;
}

void chicken::treatment()
{
  std::cout << "Second!" << std::endl;
}

void create_cow(std::vector<animal*> &vec)
{
  std::string n, l;
  std::cout << "Give me a name:";
  std::cin >> n;
  std::cout << "Give me a location:";
  std::cin >> l;
  vec.push_back(new cow(n, l));
}

void create_chicken(std::vector<animal*> &vec)
{
  std::string n, l;
  std::cout << "Give me a name:";
  std::cin >> n;
  std::cout << "Give me a location:";
  std::cin >> l;
  vec.push_back(new chicken(n, l));
}

void delete_animal(std::vector<animal*> &vec)
{
  int nr;
  std::cout << "which one?";
  std::cin >> nr;
  delete vec[nr];
}

void load_food(char** food, char** argv)
{
  int len = atoi(argv[1]);
  *food = new char[len];
  read(open(argv[2], O_RDONLY), *food, len);
}

void treatment(std::vector<animal*> &vec)
{
  int nr;
  std::cout << "which one?";
  std::cin >> nr;
  vec.at(nr)->treatment();
}

void get_info(std::vector<animal*> &vec)
{
  int nr;
  std::cout << "which one?" << std::endl;
  std::cin >> nr;
  vec.at(nr)->info();
}

int main(int argc, char** argv)
{
  std::vector<animal*> storage;
  std::cout << "Welcome, what do you want to do?" << std::endl;
  int op;
  char* food;
  std::cout << "1) create cow" << std::endl;
  std::cout << "2) create chicken" << std::endl;
  std::cout << "3) delete animal" << std::endl;
  std::cout << "4) load food for animals" << std::endl;
  std::cout << "5) treat animal" << std::endl;
  std::cout << "6) get info of animal" << std::endl;

  while(1)
  {
    std::cout << std::endl << "What will it be?";
    std::cin >> op;
    switch(op)
    {
      case 0:
        std::cout << "DEBUG MODE ON" << std::endl;
        /* this was deleted in the release version */
        break;
      case 1:
        create_cow(storage);
        break;
      case 2:
        create_chicken(storage);
        break;
      case 3:
        delete_animal(storage);
        break;
      case 4:
        load_food(&food, argv);
        break;
      case 5:
        treatment(storage);
        break;
      case 6:
        get_info(storage);
        break;
      default:
        exit(0);
        break;
    }
    std::cout << "We have " << storage.size() << " animals now" << std::endl;
  }
}
