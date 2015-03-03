__author__ = "Linus"

from simple import Copier



def quickTest(player1, player2, weights, soldiers, iterations):
    """Call like
    quickTest(Copier, CleverStrat, 10, 100, 9000)"""
    totalscore = 0 # positive for P1 winning, negative for P2 winning

    P1 = player1(weights, soldiers)
    P2 = player2(weights, soldiers)

    move1 = P1.next()
    move2 = P2.next()
    
    for i in xrange(iterations):
        totalscore += score(move1, move2, weights, soldiers)
        move1, move2 = P1.send(move2), P2.send(move1)

    return totalscore
        
def score(move1, move2, weights, soldiers):
    check(move1, weights, soldiers)
    check(move2, weights, soldiers)

    total = 0
    for i in xrange(len(weights)):
        if move1[i] > move2[i]: total += weights[i]
        if move1[i] < move2[i]: total -= weights[i]

    return total


def check(move, weights, soldiers):
    assert(all(a == int(a) for a in move))
    assert(sum(move) == soldiers)
    assert(len(move) == len(weights))
    move[0]
