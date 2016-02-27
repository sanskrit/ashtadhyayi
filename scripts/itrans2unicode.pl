#!/usr/bin/perl

# Usage:
# cat itrans.itx | ./itrans2unicode.pl > unicode.txt

# Modified version of http://sanskritdocuments.org/processing_tools/itrans2html_pl.txt
# Original Date: 09/08/2009
# Original Author: Pankaj Gupta (pankaj.gupta at yahoo.com)
# Free for public use.

%trans = (
        '.h' => 'ः',
        '{}' => '',

        # vowels
        'a' =>'अ',
        'aa' =>'आ',
        'A' =>'आ',
        'i' =>'इ',
        'ii' =>'ई',
        'I' => 'ई',
        'u' => 'उ',
        'uu' => 'ऊ',
        'U' => 'ऊ',
        'R^i' => 'ऋ',
        'RRi' => 'ऋ',
        'R^I' => 'ॠ',
        'RRI' => 'ॠ',
        'L^i' => 'ऌ',
        'LLi' => 'ऌ',
        'L^I' => 'ॡ',
        'LLI' => 'ॡ',
        'e' => 'ए',
        'ai' => 'ऐ',
        'o' => 'ओ',
        'au' => 'औ',
        'aM' => 'अं',
        'aH' => 'अः',


        # Various signs
        '.n' => 'ँ',
        'M' => 'ं',
        '.m' => 'ं',
        '.a' => 'ऽ',
        '.c' => 'ँ',
        '.N' => 'ँ',
        '{\\m+}' => 'ꣳ', # chandrabindu virama
        '.h' => '्',
        'H' => 'ः',
        'OM' => 'ॐ',
        'AUM' => 'ॐ',

#my additions
        '|' => '।',
        '||' => '॥'
);



%consonants = (
        'k' => 'क',
        'kh' => 'ख',
        'g' => 'ग',
        'gh' => 'घ',
        '~N' => 'ङ',
        'N^' => 'ङ',
        'c' => 'च',
        'ch' => 'च',
        'Ch' => 'छ',
        'chh' => 'छ',
        'j' => 'ज',
        'jh' => 'झ',
        '~n' => 'ञ',
        'JN' => 'ज्ञ',
        'T' => 'ट',
        'Th' => 'ठ',
        'D' => 'ड',
        'Dh' => 'ढ',
        'N' => 'ण',
        't' => 'त',
        'th' => 'थ',
        'd' => 'द',
        'dh' => 'ध',
        'n' => 'न',
        'p' => 'प',
        'ph' => 'फ',
        'b' => 'ब',
        'bh' => 'भ',
        'm' => 'म',
        'y' => 'य',
        'r' => 'र',
        'l' => 'ल',
        'v' => 'व',
        'w' => 'व',
        'sh' => 'श',
        'Sh' => 'ष',
        'shh' => 'ष',
        'S' => 'ष',
        'Z' => 'ष',
        's' => 'स',
        'h' => 'ह',
        'L' => 'ळ',
        'kSh' => 'क्ष',
        'x' => 'क्ष',
        'kS' => 'क्ष',
        'GY' => 'ज्ञ',
        'j~n' => 'ज्ञ',
        'dny' => 'ज्ञ',
);



# matras
%matras = (
     'aa' =>  'ा',
     'A' =>  'ा',
     'i' =>  'ि',
     'ii' =>  'ी',
     'I' =>  'ी',
     'u' =>  'ु',
     'uu' =>  'ू',
     'U' =>  'ू',
     'R^i' =>  'ृ',
     'RRi' =>  'ृ',
     'R^I' =>  'ॄ',
     'RRI' =>  'ॄ',
     'L^i' =>  'ॢ',
     'LLi' =>  'ॢ',
     'L^I' =>  'ॣ',
     'LLI' =>  'ॣ',
     'e' =>  'े',
     'ai' =>  'ै',
     'o' =>  'ो',
     'au' =>  'ौ'
);




%matraprefixes = (
     '.n' =>  '&#x0923;',
);




# add consonents to trans table
for $mykey (keys %consonants) {
    $trans{$mykey."a"} = $consonants{$mykey};
    $trans{$mykey} = $consonants{$mykey}."्";

# also add to matraprefixes
    $matraprefixes{$mykey} = $consonants{$mykey};
}

for $matra (keys %matras) {
    for $matraprefix (keys %matraprefixes) {
	$trans{$matraprefix.$matra} = $matraprefixes{$matraprefix}.$matras{$matra};
    }
}




# Actual Translation Logic:
@signs = sort {length($b) <=> length($a)} keys %trans;
@signs = map quotemeta($_), @signs;
$re = join '|', @signs, '.';


# Read Input from Stdin - one line at a time
while (<STDIN>) {
    $input = "$_";

    # Just handling a bug in some itrans texts that use 'z' instead of 'Z'. Convert any z in input to 'Z' - This can be disabled if you don't want this
    $input =~ s/z/Z/g;
    $originalinput = $input;

    # This does the actual translation for this line
    # The ##.*## is to handle english text within ##. It will leave ##abc def## as ##abc def##
    $input =~ s/(##.*##|$re)/exists($trans{$1}) ? $trans{$1} : $1/geo;

    # If you don't want the ##english text## functionality - this line can be used in place of the above line
#    $input =~ s/($re)/exists($trans{$1}) ? $trans{$1} : $1/geo;


#    $input =~ s/\&\#x094d;\&\#x094d;/\&\#x094d;/g;


    # For debugging (to see what was the itrans input):
    #print $originalinput, "<br>";

   $input =~ s/##//g;


    # Print the translated Unicode HTML
    print $input;
}



# For debug purposes just our map
#    @debugsigns = sort {$b cmp $a} keys %trans;
#    print "<table>";
#    for $sign (@debugsigns) {
#	$val = $trans{$sign};
#	$val =~ s/;//geo;
#	print "<tr><td> $sign </td><td> $trans{$sign} </td><td> $val </td></tr>";
#    }
#    print "</table>";
#  --- End of Debug ----- (safe to remove this entire debug section)
