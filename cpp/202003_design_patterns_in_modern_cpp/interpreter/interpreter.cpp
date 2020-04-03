#include <string>
#include <map>
#include <iostream>

#include <cassert>
#include <cctype>
#include <vector>
#include <sstream>


using namespace std;

struct ExpressionProcessor
{
  struct Token {
      enum Type { number, var, plus, minus } type;
      string s;

      explicit Token(Type type_, string s_) : type(type_), s(s_) {}
  };

  map<char,int> variables;
  
  vector<Token> tokenize(string s) {
      vector<Token> tokens;
      for (auto i = 0; i < s.size(); ) {
          if(s[i] == '+') {
              tokens.emplace_back(Token(Token::plus, "+"));
              ++i;
              continue;
          }
          if(s[i] == '-') {
              tokens.emplace_back(Token(Token::minus, "-"));
              ++i;
              continue;
          }
          
          if(std::isdigit(s[i])) {
              ostringstream oss;
              while (i < s.size() && std::isdigit(s[i])) {
                  oss << s[i];
                  ++i;
              }
              tokens.emplace_back(Token(Token::number, oss.str()));
              continue;   
          }

          if(std::isalpha(s[i])) {
              ostringstream oss;
              while (i < s.size() && std::isalpha(s[i])) {
                  oss << s[i];
                  ++i;
              }
              tokens.emplace_back(Token(Token::var, oss.str()));
              continue;   
          }

          return {};
      }

      return tokens;
  }
  

  int calculate(const string& expression)
  {
    auto tokens = tokenize(expression);

    for(auto x: tokens) {
        cout << x.s << " "; 
    }
    cout << "\n";

    try {
        auto result = parse(tokens);
        return result;
    } 
    catch(const std::exception &e) {
        return 0;
    }
  }

  void execute(std::vector<int>& vals, std::vector<char>& ops) {
      char op = ops.back();
      ops.pop_back();
      int val2 = vals.back();
      vals.pop_back();
      int val1 = vals.back();
      vals.pop_back();

      if (op == '-') {
          vals.push_back(val1 - val2);
          return;
      }
      if (op == '+') {
          vals.push_back(val1 + val2);
          return;
      }
  }

  int parse(vector<Token> tokens) {
    vector<int> vals;
    vector<char> ops;
    
    for (auto token : tokens) {
        if (token.type == Token::number) {
            vals.push_back(stoi(token.s));
            continue;
        }
        
        if (token.type == Token::var) {
            if (token.s.size() != 1) {
                throw runtime_error("only one char variables are supported");
            }
            vals.push_back(variables[token.s[0]]);
            continue;
        }



        if (token.type == Token::minus) {
            while (!ops.empty()) {
                execute(vals, ops);
            }
            ops.push_back('-');
            continue;
        }

        if (token.type == Token::plus) {
            while (!ops.empty()) {
                execute(vals, ops);
            }
            ops.push_back('+');
            continue;
        }

        throw logic_error("Unsupported token");
    }

    while(!ops.empty()) {
        execute(vals, ops);
    }

    if (vals.size() != 1) {
        throw runtime_error("invalid expression");
    }

    return vals[0];
  }
};


int main() {
    ExpressionProcessor ep{};

    ep.variables['x'] = 10;
    ep.variables['y'] = 20;

    assert(ep.calculate("x-2-y") == -12);

    assert(ep.calculate("1+2") == 3);

    assert(ep.calculate("ab+5") == 0);

    return 0;
}




