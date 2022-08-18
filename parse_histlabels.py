output_files = "output.csv"
#traces = [ 'wiki', 'gradle', 'scarab', 'mergep']
traces = ['gradle']

results = {}
#batch_length = 800000
batch_length = 10000


renaming = { 'adaptive.Arc' : 'ARC', 
             'linked.Fifo' : 'FIFO', 
             'linked.Lfu' : 'LFU', 
             'linked.Lru' : 'LRU', 
             'product.Caffeine' : 'Caffeine', 
             'sampled.sampled.Hyperbolic' : 'Hyperbolic',
           }

if __name__ == "__main__":
    for trace in traces:
        
        requests = None
        with open(f'output-{trace}.csv', 'r') as f:
            next(f)
            for line in f:
                line = line.split(',')
                policy = line[0]
                hits = int(line[2])
                batchHits = list(map(int, line[-1][1:-2].split(' ')))
                results[policy] = batchHits
                requests = int(line[4])
        with open(f'probahist10K-{trace}.csv', 'w') as f:
            policies = [ 'linked.Lfu', 'linked.Lru', 'sampled.sampled.Hyperbolic', 'adaptive.Arc', 'product.Caffeine' ]
            #print('Batch,' + ','.join(renaming[policy] for policy in policies), file=f)
            for i in range(requests // batch_length):
                total_hits = 0
                for policy in policies:
                    total_hits = total_hits + results[policy][i]
                if(total_hits != 0):
                #    print(','.join(str(float(results[policy][i]) / float(total_hits)) for policy in policies), file=f)
                    print(f'{batch_length * (i+1)},' + ','.join(str(float(results[policy][i])) for policy in policies), file=f)
                else:
                    print(f'{batch_length * (i+1)},' + ','.join(str(float(results[policy][i])) for policy in policies), file=f)
