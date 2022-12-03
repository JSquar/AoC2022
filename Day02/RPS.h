/*
 * File: RPS.h
 * Created: Friday, 2nd December 2022 6:33:31 pm
 * Author: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 *
 * -----
 * Last Modified: Saturday, 3rd December 2022 1:11:18 am
 * Modified By: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 * Copyright (c) 2022 Jannek Squar
 *
 */

#ifndef RPS
#define RPS

#include <list>
#include <string>

void read_input(const std::string &filename, std::list<char> &output);

int get_single_result(const char playerA, const char playerB);

int get_single_result_alternative(const char playerA, const char playerB);

int get_all_results(const std::list<char> &input,
                    int (*calc_func)(const char, const char));
#endif /* RPS */
