/*
 * File: RPS.cpp
 * Created: Friday, 2nd December 2022 6:32:28 pm
 * Author: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 *
 * -----
 * Last Modified: Saturday, 3rd December 2022 1:11:10 am
 * Modified By: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 * Copyright (c) 2022 Jannek Squar
 *
 */
#include "RPS.h"
#include <fstream>
#include <iostream>
#include <list>
#include <string>

void read_input(const std::string &filename, std::list<char> &output) {
  std::ifstream infile;
  std::string line;

  infile.open(filename);
  while (infile >> line) {
    output.push_back(line[0]);
  }

  return;
}

int get_single_result(const char playerA, const char playerB) {
  int result = 0;
  result = playerB - playerA + ('A' - 'X');
  // lost
  if (result == 2 || result == -1) {
    result = 0;
  }
  // draw
  else if (result == 0) {
    result = 3;
  }
  // win
  else if (result == 1 || result == -2) {
    result = 6;
  } else {
    std::cout << "You should not be here!\n";
    std::cout << "playerA: " << playerA << " playerB: " << playerB
              << " result: " << result << "\n";
    result = 1000;
  }

  // add selection of weapon
  result += playerB - 'W';

  return result;
}

int get_all_results(const std::list<char> &input,
                    int (*calc_func)(const char, const char)) {
  int final_result = 0;
  for (std::list<char>::const_iterator iter = input.cbegin();
       iter != input.cend(); std::advance(iter, 2)) {
    final_result += calc_func(*iter, *(std::next(iter, 1)));
  }

  return final_result;
}