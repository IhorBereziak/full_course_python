from parser_class import Parser

parser = Parser('https://www.ua-football.com/ua/sport', 'news.txt')
parser.run()
print(Parser.results)