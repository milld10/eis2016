BIN=uafeasy
CC=g++
CFLAGS=-z execstack -m32 -static -g -ggdb -O0 -fno-stack-protector -std=c++11
USER=UAF

$(BIN):
	$(CC) $(CFLAGS) -o $(BIN) $(BIN).cpp
	sudo chown $(USER):$(USER) $(BIN)
	sudo chmod u+s $(BIN)

.PHONY: clean $(BIN)

clean:
	rm -f $(BIN)
