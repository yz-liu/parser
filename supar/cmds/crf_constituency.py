# -*- coding: utf-8 -*-

import argparse

from supar import CRFConstituencyParser
from supar.cmds.cmd import parse


def main():
    parser = argparse.ArgumentParser(
        description='Create the Biaffine Parser model.'
    )
    parser.set_defaults(Parser=CRFConstituencyParser)
    parser.add_argument('--mbr', action='store_true',
                        help='whether to use mbr decoding')
    subparsers = parser.add_subparsers(title='Commands', dest='mode')
    subparser = subparsers.add_parser(
        'train',
        help='Train a parser.'
    )
    subparser.add_argument('--feat', '-f', default='char',
                           choices=['tag', 'char', 'bert'],
                           help='choices of additional features')
    subparser.add_argument('--build', '-b', action='store_true',
                           help='whether to build the model first')
    subparser.add_argument('--max-len', default=None, type=int,
                           help='max length of the sentences')
    subparser.add_argument('--train', default='data/ptb/train.pid',
                           help='path to train file')
    subparser.add_argument('--dev', default='data/ptb/dev.pid',
                           help='path to dev file')
    subparser.add_argument('--test', default='data/ptb/test.pid',
                           help='path to test file')
    subparser.add_argument('--embed', default='data/glove.6B.100d.txt',
                           help='path to pretrained embeddings')
    subparser.add_argument('--unk', default='unk',
                           help='unk token in pretrained embeddings')
    subparser.add_argument('--bert', default='bert-base-cased',
                           help='which bert model to use')
    # evaluate
    subparser = subparsers.add_parser(
        'evaluate',
        help='Evaluate the specified parser and dataset.'
    )
    subparser.add_argument('--data', default='data/ptb/test.pid',
                           help='path to dataset')
    # predict
    subparser = subparsers.add_parser(
        'predict',
        help='Use a trained parser to make predictions.'
    )
    subparser.add_argument('--prob', action='store_true',
                           help='whether to output probs')
    subparser.add_argument('--data', default='data/ptb/test.pid',
                           help='path to dataset')
    subparser.add_argument('--pred', default='pred.pid',
                           help='path to predicted result')
    parse(parser)


if __name__ == "__main__":
    main()
