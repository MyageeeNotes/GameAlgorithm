# coding: utf-8
# Coding Skills: Kadai02-4
# 課題２－４

import Kadai02 as Poker


if __name__ == "__main__":
    joker_flag = True
    data, joker_flag = Poker.initialize(joker_flag)
    name = Poker.judge(data)
    Poker.result(data, name)
