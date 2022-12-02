/*
 * File: RPS.cpp
 * Created: Friday, 2nd December 2022 6:32:28 pm
 * Author: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 *
 * -----
 * Last Modified: Friday, 2nd December 2022 7:20:10 pm
 * Modified By: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 * Copyright (c) 2022 Jannek Squar
 *
 */
#include "RPS.h"
#include <fstream>
#include <list>
#include <string>

void read_input(const std::string &filename, std::list<std::string> &output) {
  std::ifstream infile;
  std::string line;

  infile.open(filename);
  while (infile >> line) {
    output.push_back(line);
  }

  return;
}