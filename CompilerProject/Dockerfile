FROM gcc:4.9
RUN mkdir /application
WORKDIR "/application"

ADD src/helloworld.cpp /application/

RUN g++ -o Test helloworld.cpp
CMD [ "./Test" ]
