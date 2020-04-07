/*
 * "one or more rats attacks a player.
 * rat has an attack== 1.
 * If rats attack as a swarm, then each rat's attack is equal to the total number of rats in play.
 * rat enters play through the constructor and leaves play via its destructor,
 */
#include <gtest/gtest.h>

#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>

using namespace std;

struct IRat {
    virtual void set_attack(int value) = 0;

    virtual ~IRat() = default;
};

struct Game
{
    vector<IRat*> rats;

    void subscribe(IRat* rat) {
        rats.push_back(rat);
        for( auto r: rats) {
            r->set_attack(rats.size());
        }
    }

    void unsubscribe(IRat* rat) {
        rats.erase(std::remove(rats.begin(), rats.end(), rat), rats.end());
        for( auto r: rats) {
            r->set_attack(rats.size());
        }
    }
};

struct Rat : IRat
{
    Game& game;
    int attack{1};

    Rat(Game &game) : game(game)
    {
        game.subscribe(this);
    }

    ~Rat() override
    {
        game.unsubscribe(this);
    }

    void set_attack(int value) override {
        attack = value;
    }
};


namespace {
class ObserverTests: public ::testing::Test {
protected:
    void SetUp() override {
        cout << "ObserverTests::setUp\n";
    }
};
    TEST_F(ObserverTests, test1) {
        Game game;
        auto rat1 = make_shared<Rat>(game);
        ASSERT_EQ(1, rat1->attack);

        auto rat2 = make_shared<Rat>(game);
        auto rat3 = make_shared<Rat>(game);
        ASSERT_EQ(3, rat1->attack);
        ASSERT_EQ(3, rat2->attack);
        ASSERT_EQ(3,rat3->attack);

        rat1.reset();
        ASSERT_EQ(2, rat2->attack);
        ASSERT_EQ(2, rat3->attack);
    }

}

int main(int ac, char *av[]) {
    testing::InitGoogleTest(&ac, av);
    return RUN_ALL_TESTS();
}