# coding: utf-8
# Coding Skills: Kadai02
# 345(30)

from FriAM_CodingSkills.Kadai02_Poker import Kadai02 as Poker


if __name__ == "__main__":
    joker_flag = True
    data, joker_flag = Poker.initialize(joker_flag)
    name = Poker.judge(data)
    Poker.result(data, name)