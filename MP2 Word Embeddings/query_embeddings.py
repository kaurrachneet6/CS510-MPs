from numpy.linalg import norm
import metapy
from svd_embeddings import SVDEmbeddings
import sys

def top_k(w_x, w_y, w_z):
    x = glove.at(w_x)[0]
    y = glove.at(w_y)[0]
    z = glove.at(w_z)[0]

    query = svd_embeddings.at(y) - svd_embeddings.at(x) + svd_embeddings.at(z)
    query /= norm(query, 2)

    for result in svd_embeddings.top_k(query, k=10):
        word = glove.term(result[0])
        sim = result[1]
        print("{} ({})".format(word, sim))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} embedding_file".format(sys.argv[0]))
        sys.exit(1)

    glove = metapy.embeddings.load_embeddings('config.toml')
    svd_embeddings = SVDEmbeddings(sys.argv[1])

    while True:
        words = input('Input analogy (X is to Y as Z is to _) as X Y Z: ')
        if len(words) == 0:
            break

        query = words.split(' ')

        if len(query) != 3:
            print('Please input three words.\n')
        else:
            top_k(*query)
            print()
