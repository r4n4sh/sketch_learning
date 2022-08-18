output_files = "output.csv"
traces = [ 'wiki', 'gradle', 'scarab' ]


if __name__ == "__main__":
    for trace in traces:
        
        with open(f'parsed-mergep.csv', 'r') as f:
            next(f)
            for line in f:
                line = line.split(',')
                policies_list = []
                policies_list.append(line[1])
                policies_list.append(line[2])
                policies_list.append(line[3])
                policies_list.append(line[4])
                policies_list.append(line[5])


                total_hits = sum(int(i) for i in policies_list)
                print('total_hits: ', total_hits)
                print('line : ', line)

                if(total_hits != 0):
                    print(','.join(str(float(int(i)) / float(total_hits)) for i in policies_list))
                else:
                    print(','.join(str(float(int(i))) for i in policies_list))

