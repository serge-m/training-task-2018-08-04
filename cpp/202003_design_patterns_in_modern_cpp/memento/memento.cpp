#include <iostream>
#include <vector>
#include <memory>
#include <cassert>

using namespace std;
/*
 * "A TokenMachine  is in charge of keeping tokens.
 * Each Token  is a reference type with a single numerical value.
 * The machine supports adding tokens and, when it does,
 * it returns a memento representing the state of that system at that given time.

You are asked to fill in the gaps and implement
 the Memento design pattern for this scenario.
 Pay close attention to the situation where
 a token is fed in as a smart pointer and
 its value is subsequently changed on that pointer -
 you still need to return the correct system snapshot!"

 */
struct Token
{
    int value;

    Token(int value) : value(value) {}
};

struct Memento
{
    vector<shared_ptr<Token>> tokens;
};

struct TokenMachine
{
    vector<shared_ptr<Token>> tokens;

    Memento add_token(int value)
    {
        return add_token(make_shared<Token>(value));
    }

    // adds the token to the set of tokens and returns the
    // snapshot of the entire system
    Memento add_token(const shared_ptr<Token>& token)
    {
        tokens.push_back(token);
        Memento m{};
        for(const auto& t: tokens) {
            m.tokens.emplace_back(make_shared<Token>(*t));
        }
        return m;
    }

    // reverts the system to a state represented by the token
    void revert(const Memento& m)
    {
        tokens.clear();
        for(const auto& t: m.tokens) {
            tokens.emplace_back(make_shared<Token>(*t));
        }
    }
};


void print(const TokenMachine &tm);

bool equal_tokens(const vector<shared_ptr<Token>>& tokens1, const vector<Token>& tokens2);

int main() {
    TokenMachine tm{};

    auto m1 = tm.add_token(10);
    assert(equal_tokens(tm.tokens, {10}));
    auto m2 = tm.add_token(20);
    assert(equal_tokens(tm.tokens, {10, 20}));
    tm.revert(m1);
    assert(equal_tokens(tm.tokens, {10}));

    auto st = make_shared<Token>(30);
    auto m3 = tm.add_token(st);
    assert(equal_tokens(tm.tokens, {10, 30}));
    auto m4 = tm.add_token(40);
    assert(equal_tokens(tm.tokens, {10, 30, 40}));
    st->value = 31;
    assert(equal_tokens(tm.tokens, {10, 31, 40}));
    tm.revert(m3);
    assert(equal_tokens(tm.tokens, {10, 30}));
    tm.tokens[1]->value = 32;
    assert(equal_tokens(tm.tokens, {10, 32}));
    tm.revert(m3);
    assert(equal_tokens(tm.tokens, {10, 30}));
    tm.revert(m4);
    assert(equal_tokens(tm.tokens, {10, 30, 40}));



    return 0;
}

void print(const TokenMachine &tm) {
    for(const auto& it: tm.tokens) {
        cout << it->value << " ";
    }
    cout << "\n";
}

bool equal_tokens(const vector<shared_ptr<Token>> &tokens1, const vector<Token> &tokens2) {
    if (tokens1.size() != tokens2.size())
        return false;
    for(size_t i = 0; i < tokens1.size() && i < tokens2.size(); ++i) {
        if (tokens1[i]->value != tokens2[i].value)
            return false;
    }
    return true;
}
