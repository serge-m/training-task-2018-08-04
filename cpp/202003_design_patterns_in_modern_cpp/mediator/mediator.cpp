#include <vector>
#include <iostream>
#include <cassert>

/*
"Mediator
 There is any number of instances of Participant  classes.
 Each Participant has a value, initially zero.
A participant can call say(), which is broadcast to all other participants.
 every other participant is obliged to increase their value  by the value being broadcast.

    p1.say(3);
    assert(p1.value==0);
    assert(p2.value==3);

    p2.say(2);
    assert(p1.value==2);
    assert(p2.value==3);
 */


using namespace std;

struct IParticipant {
    virtual void increment(int value) = 0;
    virtual ~IParticipant() = default;;
};

struct Mediator {
    vector<IParticipant*> participants;

    void broadcast(const IParticipant* sender, int value) {
        for (auto p : participants) {
            if (p == sender) {
                continue;
            }
            p->increment(value);
        }
    }
};

struct Participant : IParticipant
{
    int value{0};
    Mediator& mediator;

    Participant(Mediator &mediator) : mediator(mediator)
    {
      mediator.participants.push_back(this);
    }

    void say(int val)
    {
        mediator.broadcast(this, val);
    }

    void increment(int i) override {
        value += i;
    }
};



int main() {
    Mediator m;
    Participant p1(m);
    Participant p2(m);
    p1.say(3);
    assert(p1.value==0);
    assert(p2.value==3);

    p2.say(2);
    assert(p1.value==2);
    assert(p2.value==3);

    cout << "done\n";
    return 0;
}
