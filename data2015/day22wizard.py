class Combat:

    def __init__(self, actions):
        self.p_hp = 0
        self.b_hp = 0
        self.p_mp = 0
        self.p_def = 0
        self.b_att = 0
        self.b_pois = 0
        self.recharge = 0
        self.total_mana_used = 0
        self.t = 1
        self.effects = {i: [] for i in range(100)}
        self.actions = actions
        self.death = False
        self.player_win = None

    def set_player_stats(self, hp, mp):
        self.p_hp = hp
        self.p_mp = mp

    def set_boss_stats(self, hp, att):
        self.b_hp = hp
        self.b_att = att

    def use_mana(self, mana):
        self.p_mp -= mana
        self.total_mana_used += mana

    def check_if_death(self):
        if self.p_hp > 0 and self.b_hp > 0:
            return False
        else:
            if self.p_hp <= 0:
                self.player_win = False
                print('player died')
            if self.b_hp <= 0:
                self.player_win = True
                print('boss died')
            self.death = True
            return True

    def check_effect_deactivation(self):
        for effect in self.effects[self.t]:
            if effect == 's':
                self.p_def -= 7
            if effect == 'p':
                self.b_pois -= 3
            if effect == 'r':
                self.recharge -= 101

    def do_player_turn(self):

        # at start of my turn, get any recharge coming, deal any poison damage
        self.p_mp += self.recharge
        self.b_hp -= self.b_pois
        self.check_if_death()
        if self.death:
            return

        # check to see if any instance of shield, poison, or recharge deactivate this turn
        self.check_effect_deactivation()

        # do the next action in our list
        action = self.actions[0]
        if action == 'm':
            self.use_mana(53)
            self.b_hp -= 4
        if action == 'd':
            self.use_mana(73)
            self.b_hp -= 2
            self.p_hp += 2
        if action == 's':
            self.use_mana(113)
            self.p_def += 7
            self.effects[self.t+6].append('s')
        if action == 'p':
            self.use_mana(173)
            self.effects[self.t+6].append('p')
            self.b_pois += 3
        if action == 'r':
            self.use_mana(229)
            self.effects[self.t+5].append('r')
            self.recharge += 101

        # player turn over
        self.t += 1
        self.check_if_death()
        if self.death:
            return
        self.actions = self.actions[1:]

    def do_boss_turn(self):

        # at the start of his turn, take any poison damage, get any recharge
        self.b_hp -= self.b_pois
        self.p_mp += self.recharge

        self.check_if_death()
        if self.death:
            return

        # check to see if anything deactivates
        self.check_effect_deactivation()

        # attack
        self.p_hp -= max([1, self.b_att - self.p_def])

        # boss turn over
        self.t += 1
        self.check_if_death()
        if self.death:
            return

    def display_status(self):

        print(f'Turn {self.t}')
        print(f'Player:\tHP\tMP\tDef')
        print(f'\t\t{self.p_hp}\t{self.p_mp}\t{self.p_def}')
        print(f'Boss:\tHP\tAtt')
        print(f'\t\t{self.b_hp}\t{self.b_att}')
        print()

    def do_whole_fight(self):
        for i in range(len(self.actions)):
            self.do_player_turn()
            if self.death:
                return 1 if self.player_win else 0
            self.do_boss_turn()
            if self.death:
                return 1 if self.player_win else 0
        return -1



# actions1 = ['p', 'm']
# actions2 = ['r', 's', 'd', 'p', 'm']
# actions = actions2
# combat = Combat(actions)
# combat.set_player_stats(10, 250)
# combat.set_boss_stats(14, 8)
# combat.display_status()
# for i in range(len(actions)):
#     print(f'Player turn: action {actions[i]}')
#     combat.do_player_turn()
#     combat.display_status()
#     if not combat.death:
#         print(f'Boss turn')
#         combat.do_boss_turn()
#         combat.display_status()
# print(combat.effects)

actions2 = ['r', 's', 'd', 'p', 'm']
actions = actions2
combat = Combat(actions)
result = combat.do_whole_fight()
if result == 1:
    print(f'won with mana cost:  {combat.total_mana_used}')
elif result == 0:
    print('lost')
else:
    print('lost - ran out of steps')