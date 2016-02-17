from glob import glob
from operator import itemgetter


def main():
    for outpath in glob("data/output/vocab_*"):
        with open(outpath + "/pairs.txt") as f:
            pairs = []
            for line in f:
                fields = line.split()
                if len(fields) == 1:
                    word1 = fields[0]
                elif len(fields) == 2:
                    word2, score = fields
                    pairs.add((word1, word2, score))
                else:
                    raise IOError("Wrong number of fields: " + " ".join(fields))
        with open(outpath + "/pairs_sorted.csv", "w") as f:
            f.writelines(",".join(p) + "\n" for p in sorted(
                pairs, key=itemgetter(2), reverse=True))
        # My attempt to run the distance utility interactively from Python failed.
        # Use generate_pairs_file.sh instead and then run this script.
        # with open(outpath + "/vocab.txt") as f:
        #     vocab = f.readlines()
        # for model in glob(outpath + "/*.bin"):
        #     with subprocess.Popen(["./word2vec/distance", model],
        #                           stdout=subprocess.PIPE,
        #                           stdin=subprocess.PIPE) as p:
        #         pairs = []
        #         for word in vocab:
        #             p.stdout.read()
        #             p.stdin.write(word.encode())
        #             neighbors = map(str.split, p.stdout.readlines()[2:])
        #             pairs += [tuple([word] + n) for n in neighbors]
        #         p.stdin.write("EXIT\n")
        # with open(outpath + os.path.splitext(model)[0] + "_pairs.csv") as f:
        #     f.writelines(",".join(p) + "\n" for p in sorted(
        #         pairs, key=itemgetter(2), reverse=True))


if __name__ == "__main__":
    main()
