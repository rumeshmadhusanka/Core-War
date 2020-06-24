# Core-War

The Core War game appeared in article by Alexander Dewdney published in May 1984 in the Scientic American. The principle of this game
is extremely simple: two or more computer programs are loaded into the memory of a virtual machine (i.e. of a program that simulates a
computer) and are executed concurrently, one instruction at a time. The goal of a process is to be the last one alive. In order to do so, a
program has to do everything it can to eliminate the opposing processes. The whole point of the game comes from the fact that a program
can write anywhere in memory and can therefore cause the elimination of other players by writing an illegal instruction in the code of the
latter. A program can also move and duplicate itself in the memory, to escape from its opponent.
