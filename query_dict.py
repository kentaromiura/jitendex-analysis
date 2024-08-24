import sqlite3
import zstandard as zstd
import io



if __name__ == '__main__':
    import sys
    import os
    import os.path
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("dbpath", nargs='?', help="path to the database")
    parser.add_argument("dictionary", nargs='?', help="path to the dictionary")
    parser.add_argument("query", nargs='?', help="query to the db")
    args = parser.parse_args()
    conn = sqlite3.connect(args.dbpath)

    query = """SELECT [d].definition
    FROM terms
    LEFT JOIN definitions d
    ON d.id = [terms].definition
    WHERE "term" = ? """
    cur = conn.cursor()
    cur.execute(query, (args.query,))
    rows = cur.fetchall()
    conn.close()

    fdict = open(args.dictionary, 'rb')
    zdict = fdict.read()
    dict_data = zstd.ZstdCompressionDict(zdict)
    dctx = zstd.ZstdDecompressor(dict_data=dict_data)

    index = 1
    print("\n*****************\n")
    for row in rows:
        print("Result ", index, "\n=====================\n")
        index = index + 1

        print(dctx.decompress(row[0]).decode('UTF-8'))
