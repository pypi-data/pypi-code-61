from .primitive import AllParser, ManyParser, FirstParser, AnyParser, CharParser, VoidParser, ManyOneParser

class WordParser( AllParser ):
    def __init__( self, word ):
        super().__init__( * [ CharParser( x ) for x in word ] )

    def parse(self, strinput):
        result = super().parse( strinput )
        return result.map( lambda x : "".join( x ) )

class CharSetParser( FirstParser ):
    def __init__( self, chars ):
        super().__init__( * [ CharParser( x ) for x in chars ] )

class WordSetParser( FirstParser ):
    def __init__( self, *words ):
        super().__init__( * [ WordParser( x ) for x in words ] )

class WhiteSpaceParser( CharSetParser ):
    def __init__(self):
        super().__init__( "\t\r\n " )

class WhiteSpacesParser( ManyParser ):
    def __init__(self):
        super().__init__( WhiteSpaceParser() )

class AlphaParser( AnyParser ):
    def __init__( self, plus ):
        self.plus = plus

    def parse(self, strinput):
        result = super().parse(strinput)
        return result.check( lambda x : x.isalpha() or x in self.plus )

class AlnumParser( AnyParser ):
    def __init__( self, plus ):
        self.plus = plus

    def parse(self, strinput):
        result = super().parse(strinput)
        return result.check( lambda x : x.isalnum() or x in self.plus )

class DigitParser( AnyParser ):
    def parse(self, strinput):
        result = super().parse(strinput)
        return result.check( lambda x : x.isdigit() )

class IntParser( AllParser ):
    def __init__(self):
        super().__init__(
            FirstParser( CharParser("-"), CharParser("+"), VoidParser( result = "+" ) ),
            WhiteSpacesParser(),
            ManyOneParser( DigitParser() )
        )

    def parse(self, strinput):
        result = super().parse(strinput)
        return result.map( lambda x : int( x[0] + "".join( x[2] ) ) )

class IdentParser( AllParser ):
    def __init__(self):
        super().__init__(
            AlphaParser( "_" ),
            ManyParser( AlnumParser( "_" ) )
        )

    def parse(self, strinput):
        result = super().parse(strinput)
        return result.map( lambda x : "".join( [ x[0] ] + x[1] ) )

class WrapParser( AllParser ):
    def __init__( self, wrappers, parser ):
        super().__init__(
            WordParser( wrappers[0] ),
            parser,
            WordParser( wrappers[1] )
        )

    def parse(self, strinput):
        result = super().parse(strinput)
        return result.map( lambda x : x[1] )
    parens       = "(", ")"
    curly        = "{", "}"
    square       = "[", "]"
    angled       = "<", ">"
    thick_parens = "(|", "|)"
    thick_curly  = "{|", "|}"
    thick_square = "[|", "|]"
    thick_angled = "<|", "|>"

class PadParser( AllParser ):
    def __init__( self, parser, **args ):
        padding = args.get( "pad", "lr" )
        super().__init__(
            WhiteSpacesParser() if "l" in padding else VoidParser(),
            parser,
            WhiteSpacesParser() if "r" in padding else VoidParser(),
        )

    def parse(self, strinput):
        result = super().parse(strinput)
        return result.map( lambda x : x[1] )
