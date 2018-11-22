import math
import timeit
import argparse
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import util
import wrapper as wrp
import dataset
import brute_force as bf
import nearest_neighbor as nn
import nearest_insertion as ni
import cheapest_insertion as ci
import minimum_spanning_tree as mst


def validate(path, cost, adj):
    ccost = 0
    for i in range(len(path)-1):
        ccost += adj[path[i]][path[i+1]]
    ccost += adj[0][path[0]]  # first edge
    ccost += adj[util.last(path)][0] # last edge

    if not math.isclose(cost, ccost):
        raise Exception('Badly calculated path cost.')


def analyse_algorithm(adj,order,algorithm,repeat=10):
    print('\n'+algorithm.name)
    closure = algorithm.get_closure(adj, order)
    times = timeit.repeat(closure, number=1, repeat=repeat)
    min_time = min(times)

    print('procedure repeated {} times'.format(repeat))
    print('minimum time: {}'.format(min_time))
    path, cost = closure()

    return min_time, cost


def init_plots(algorithms):
    # Configure plotting
    plt.tight_layout()
    fig_correct, plot_correct = plt.subplots()
    fig_complex, plot_complex = plt.subplots()

    plot_correct.set_title('Correctness')
    plot_complex.set_title('Complexity')

    handles = []
    for algorithm in algorithms:
        handles.append(patches.Patch(color=algorithm.color , label=algorithm.name))

    handles.append(patches.Patch(color='white', label='x = n'))
    handles_correct = handles.copy()
    handles_correct.append(patches.Patch(color='white',alpha=0, label='y = path cost'))
    handles_complex = handles.copy()
    handles_complex.append(patches.Patch(color='white', alpha=0, label='y = min running time after 10 repeats'))
    plot_correct.legend(loc='upper left',title='Legend', handles=handles_correct, fontsize='x-small')
    plot_complex.legend(loc='upper left', title='Legend', handles=handles_complex, fontsize='x-small')

    plot_correct.set_xlabel("x")
    plot_correct.set_ylabel("y")
    plot_complex.set_xlabel("x")
    plot_complex.set_ylabel("y")

    return fig_correct, fig_complex, plot_correct, plot_complex


def main(args):
    # Determine which algorithms to perform
    algorithms = []
    if args.bf:
        algorithms.append(wrp.AlgorithmWrapper(bf.CONTENT))
    if args.nn :
        algorithms.append(wrp.AlgorithmWrapper(nn.CONTENT))
    if args.ni :
        algorithms.append(wrp.AlgorithmWrapper(ni.CONTENT))
    if args.mst:
        algorithms.append(wrp.AlgorithmWrapper(mst.CONTENT))
    if args.ci:
        algorithms.append(wrp.AlgorithmWrapper(ci.CONTENT))

    # Initialize plots
    fig_correct, fig_complex, plot_correct, plot_complex = init_plots(algorithms)

    # Execute correct command
    if args.cmd == 'read':
        for algorithm in algorithms:
            adj, order = dataset.read(args.path)
            y1, y2 = analyse_algorithm(adj,order,algorithm,args.repeat)
            plot_correct.scatter(order, y2, color=algorithm.color, alpha=0.5, s=0.5)
            plot_complex.scatter(order, y1, color=algorithm.color, alpha=0.5,s=0.5)

        fig_correct.savefig('Correctness',dpi=300,bbox_inches='tight')
        fig_complex.savefig('Complexity',dpi=300,bbox_inches='tight')

    elif args.cmd == 'random':
            if args.growth == 'logn':
                growth = util.logarithmic
            elif args.growth == 'n':
                growth = util.linear

            order = args.order  # reset n
            while order <= args.max:
                for i in range(args.trials):
                    adj = dataset.generate(order,args.spread,args.path)
                    for algorithm in algorithms:
                        y1, y2 = analyse_algorithm(adj,order,algorithm,args.repeat)
                        algorithm.x.append(order)
                        algorithm.complex.append(y1)
                        algorithm.working_complex.append(y1)
                        algorithm.correct.append(y2)
                        algorithm.working_correct.append(y2)

                for algorithm in algorithms:
                    algorithm.avg_correct.append(util.average(algorithm.working_correct))
                    algorithm.avg_complex.append(util.average(algorithm.working_complex))
                    algorithm.avg_x.append(order)
                    algorithm.working_correct.clear()
                    algorithm.working_complex.clear()

                order = growth(order)

            if args.plot:
                for algorithm in algorithms:
                    # Plot correctness measure
                    plot_correct.scatter(algorithm.x, algorithm.correct, color=algorithm.color, alpha=0.5, s=0.5)
                    plot_correct.plot(algorithm.avg_x, algorithm.avg_correct, '-', color=algorithm.color, linewidth=0.5)
                    fig_correct.savefig('Correctness', dpi=300, bbox_inches='tight')

                    # Plot complexity measure
                    plot_complex.scatter(algorithm.x, algorithm.complex, color=algorithm.color,alpha=0.5,s=0.5)
                    plot_complex.plot(algorithm.avg_x, algorithm.avg_complex, '-', color=algorithm.color, linewidth=0.5)
                    fig_complex.savefig('Complexity', dpi=300, bbox_inches='tight')


def init_parser_common(parser):
    parser.add_argument('--plot', action='store_true',default=False, required=False)
    parser.add_argument('--repeat', type=int, required=False, default=10)
    parser.add_argument('--bf',action='store_true',default=False, required=False)
    parser.add_argument('--nn',action='store_true',default=False, required=False)
    parser.add_argument('--ni',action='store_true',default=False, required=False)
    parser.add_argument('--ci',action='store_true',default=False, required=False)
    parser.add_argument('--mst',action='store_true',default=False, required=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser() # top level parser
    subparsers = parser.add_subparsers(dest="cmd", required=False)
    subparsers.required = False

    random_parser = subparsers.add_parser('random')
    random_parser.add_argument('-order', type=int, required=True)
    random_parser.add_argument('--growth', type=str, choices=['logn', 'n'], default='n')
    random_parser.add_argument('-max', type=int, required=True)
    random_parser.add_argument('--trials', type=int, default=1, required=False)
    random_parser.add_argument('-spread', type=int, required=True)
    random_parser.add_argument('--path', type=str, required=False)
    init_parser_common(random_parser)

    read_parser = subparsers.add_parser('read')
    read_parser.add_argument('-path', type=str, required=True)
    init_parser_common(read_parser)

    args = parser.parse_args()

    main(args)



