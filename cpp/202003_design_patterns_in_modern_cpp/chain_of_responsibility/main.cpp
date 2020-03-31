#include <iostream>
#include <vector>
using namespace std;

struct Creature;
struct Game {
    vector<Creature *> creatures;
};

struct StatQuery {
    enum Statistic { attack, defense } statistic;
    int result;
};

struct Creature {
   protected:
    Game &game;
    int base_attack, base_defense;

   public:
    Creature(Game &game, int base_attack, int base_defense)
        : game(game), base_attack(base_attack), base_defense(base_defense) {}
    virtual int get_attack() = 0;
    virtual int get_defense() = 0;
    virtual void query(Creature const *c, StatQuery &q){};
};

class Goblin : public Creature {
   public:
    Goblin(Game &game, int base_attack, int base_defense)
        : Creature(game, base_attack, base_defense) {}

    Goblin(Game &game) : Creature(game, 1, 1) {}

    int get_attack() override {
        StatQuery q{StatQuery::attack, base_attack};

        for (auto creature : game.creatures) {
            creature->query(this, q);
        }
        return q.result;
    }

    int get_defense() override {
        StatQuery q{StatQuery::defense, base_defense};

        for (auto creature : game.creatures) {
            creature->query(this, q);
        }
        return q.result;
    }

    void query(Creature const *c, StatQuery &q) override {
        if (q.statistic == StatQuery::defense 
             && this != c
             && dynamic_cast<Goblin const *>(c) != nullptr
        ) {
                q.result += 1;
        }
        Creature::query(c, q);
    }
};

class GoblinKing : public Goblin {
   public:
    GoblinKing(Game &game) : Goblin(game, 3, 3) {}

    // todo
    void query(Creature const *c, StatQuery &q) override {
        if (
            this != c 
            && q.statistic == StatQuery::attack
            && dynamic_cast<Goblin const *>(c) != nullptr
        ) {
            q.result += 1;
        }
        Goblin::query(c, q);
    }
};

class Elf : public Creature {
    // dummy creature without overrides. Should not influence goblins
public:
    Elf(Game &game) : Creature(game, 2, 0) {}
    int get_attack() override {
        StatQuery q{StatQuery::attack, base_attack};

        for (auto creature : game.creatures) {
            creature->query(this, q);
        }
        return q.result;
    }
    int get_defense() override {
        StatQuery q{StatQuery::attack, base_defense};

        for (auto creature : game.creatures) {
            creature->query(this, q);
        }
        return q.result;
    }

};

#include "gtest/gtest.h"

namespace
{
  class Evaluate : public testing::Test
  {
  public:
  };

  TEST_F(Evaluate, ManyGoblinsTest)
  {
    Game game;
    Goblin goblin{game};
    game.creatures.push_back(&goblin);

    cout << "Checking that a baseline goblin is a 1/1...\n";

    ASSERT_EQ(1, goblin.get_attack());
    ASSERT_EQ(1, goblin.get_defense());

    cout << "Adding a second goblin, now they should be 1/2...\n";
    Goblin goblin2{game};
    game.creatures.push_back(&goblin2);

    ASSERT_EQ(1, goblin.get_attack());
    ASSERT_EQ(2, goblin.get_defense());

    cout << "Adding a goblin king, now a goblin should be 2/3...\n";
    GoblinKing goblin3{game};
    game.creatures.push_back(&goblin3);

    ASSERT_EQ(2, goblin.get_attack());
    ASSERT_EQ(3, goblin.get_defense());
    
  }


  TEST_F(Evaluate, GoblinsAndElfsTest)
  {
    Game game;
    Goblin goblin{game};
    Elf elf{game};
    Elf elf2{game};

    game.creatures.push_back(&elf);
    game.creatures.push_back(&elf2);
    game.creatures.push_back(&goblin);

    cout << "Checking that a baseline goblin is a 1/1...\n";

    ASSERT_EQ(1, goblin.get_attack());
    ASSERT_EQ(1, goblin.get_defense());

    cout << "Adding a second goblin, now they should be 1/2...\n";
    Goblin goblin2{game};
    game.creatures.push_back(&goblin2);

    ASSERT_EQ(1, goblin.get_attack());
    ASSERT_EQ(2, goblin.get_defense());

    cout << "Adding a goblin king, now a goblin should be 2/3...\n";
    GoblinKing goblin3{game};
    game.creatures.push_back(&goblin3);

    ASSERT_EQ(2, goblin.get_attack());
    ASSERT_EQ(3, goblin.get_defense());

    ASSERT_EQ(2, elf.get_attack());
    ASSERT_EQ(0, elf.get_defense());
  }

} // namespace

int main(int ac, char* av[])
{
  testing::InitGoogleTest(&ac, av);
  return RUN_ALL_TESTS();
}