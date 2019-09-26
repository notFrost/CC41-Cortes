while True:
    relax = master.relax()
    relax.optimize()
    pi = [c.Pi for c in relax.getConstrs()]
    knapsack = Model("KP")
    knapsack.ModelSense=-1
    y = {}
    for i in range(m):
        y[i] = knapsack.addVar(ub=q[i], vtype="I", name="y[%d]"%i)
    knapsack.update()
    knapsack.addConstr(quicksum(w[i]*y[i] for i in range(m)) <= B, "width")
    knapsack.setObjective(quicksum(pi[i]*y[i] for i in range(m)), GRB.MAXIMIZE)
    knapsack.optimize()
    if knapsack.ObjVal < 1+EPS:
        break
    pat = [int(y[i].X+0.5) for i in y]
    t.append(pat)
    col = Column()
    for i in range(m):
        if t[K][i] > 0:
            col.addTerms(t[K][i], orders[i])
    x[K] = master.addVar(obj=1, vtype="I", name="x[%d]"%K, column=col)
    master.update()
    K += 1


master.optimize()
rolls = []
for k in x:
    for j in range(int(x[k].X + .5)):
        rolls.append(sorted([w[i] for i in range(m) if t[k][i]>0 for j in range(t[k][i])]))
rolls.sort()
return rolls


t = []
m = len(w)
for i in range(m):
    pat = [0]*m
    pat[i] = int(B/w[i])
    t.append(pat)