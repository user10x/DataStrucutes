def solution(queries):
    from collections import defaultdict
    import heapq
    account_map = defaultdict(int)
    activity_map = defaultdict(int)

    res = []
    for query in queries:
        if len(query) == 3:
            op, ts, acc = query
            if op == 'CREATE_ACCOUNT':
                if acc not in account_map:
                    account_map.setdefault("acc", 0)
                    res.append("true")
                else:
                    activity_map[acc]+=1
                    res.append("false")
            else:
                # TOP ACTIVITY
                op, ts, top = query
                max_heap =[(-count,acc) for acc, count in activity_map.items()]
                heapq.heapify(max_heap)
                new_res = heapq.nlargest(int(top), max_heap)
                out = ""
                for count, acc in new_res:
                    amt = account_map[acc]
                    out += f'{acc}({amt})'

                res.append(out)


        else:
            op, ts, acc, amt = query
            if op == 'DEPOSIT':
                if acc not in account_map:
                    res.append('')
                else:

                    account_map[acc] += int(amt)
                    res.append(str(account_map[acc]))
                    activity_map[acc]+=1

            else:
                if acc not in account_map:
                    res.append("")
                else:
                    remaining = account_map[acc]-int(amt)
                    if remaining >=0:
                         account_map[acc] = remaining
                         res.append(str(account_map[acc]))
                         activity_map[acc]+=1
                    else:
                         res.append("")
    return res








"""
Input
Return Value
Console Output
Error Output
queries:
[["CREATE_ACCOUNT","1","account1"],
 ["CREATE_ACCOUNT","2","account2"]]

 queries:
[
 ["CREATE_ACCOUNT","1","acc1"],
 ["CREATE_ACCOUNT","2","acc2"],
 ["CREATE_ACCOUNT","3","acc3"],
 ["CREATE_ACCOUNT","4","acc4"],
 ["CREATE_ACCOUNT","5","acc5"],
 ["CREATE_ACCOUNT","6","acc6"],
 ["CREATE_ACCOUNT","7","acc7"],
 ["CREATE_ACCOUNT","8","acc8"],
 ["CREATE_ACCOUNT","9","acc9"],
 ["CREATE_ACCOUNT","10","acc10"],
 ["DEPOSIT","11","acc0","928"],
 ["DEPOSIT","12","acc1","741"],
 ["DEPOSIT","13","acc2","703"],
 ["DEPOSIT","14","acc3","806"],
 ["DEPOSIT","15","acc4","785"],
 ["DEPOSIT","16","acc5","902"],
 ["DEPOSIT","17","acc6","927"],
 ["DEPOSIT","18","acc7","155"],
 ["DEPOSIT","19","acc8","267"],
 ["DEPOSIT","20","acc9","691"],
 ["DEPOSIT","21","acc0","651"],
 ["DEPOSIT","22","acc1","870"],
 ["DEPOSIT","23","acc2","927"],
 ["DEPOSIT","24","acc3","104"],
 ["DEPOSIT","25","acc4","894"],
 ["DEPOSIT","26","acc5","336"],
 ["DEPOSIT","27","acc6","587"],
],


"""