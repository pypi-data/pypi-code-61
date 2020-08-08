import os

from click.testing import CliRunner

from iseq import cli
from iseq.example import example_filepath
from iseq.testing import assert_same_file

_desired_output = """##gff-version 3
Homoserine_dh-consensus	iseq	.	1	519	0.0	+	.	ID=item1;Target_alph=dna;Profile_name=Homoserine_dh;Profile_alph=dna;Profile_acc=PF00742.20;Window=0;Bias=0.2;E-value=2.3e-86;Epsilon=0.01;Score=274.3
AA_kinase-consensus	iseq	.	1	723	0.0	+	.	ID=item2;Target_alph=dna;Profile_name=AA_kinase;Profile_alph=dna;Profile_acc=PF00696.29;Window=0;Bias=4.3;E-value=6.3e-107;Epsilon=0.01;Score=342.7
23ISL-consensus	iseq	.	1	486	0.0	+	.	ID=item3;Target_alph=dna;Profile_name=23ISL;Profile_alph=dna;Profile_acc=PF16620.6;Window=0;Bias=12.1;E-value=4.5e-92;Epsilon=0.01;Score=292.7
"""

_desired_ocodon = """>item1
CCTATCATTTCGACGCTCAAGGAGTCGCTGACAGGTGACCGTATTACTCGAATCGAAGGG
ATATTAAACGGCACCCTGAATTACATTCTCACTGAGATGGAGGAAGAGGGGGCTTCATTC
TCTGAGGCGCTGAAGGAGGCACAGGAATTGGGCTACGCGGAAGCGGATCCTACGGACGAT
GTGGAAGGGCTAGATGCTGCTAGAAAGCTGGCAATTCTAGCCAGATTGGCATTTGGGTTA
GAGGTCGAGTTGGAGGACGTAGAGGTGGAAGGAATTGAAAAGCTGACTGCCGAAGATATT
GAAGAAGCGAAGGAAGAGGGTAAAGTTTTAAAACTAGTGGCAAGCGCCGTCGAAGCCAGG
GTCAAGCCTGAGCTGGTACCTAAGTCACATCCATTAGCCTCGGTAAAAGGCTCTGACAAC
GCCGTGGCTGTAGAAACGGAACGGGTAGGCGAACTCGTAGTGCAGGGACCAGGGGCTGGC
GCAGAGCCAACCGCATCCGCTGTACTCGCTGACCTTCTC
>item2
AAACGTGTAGTTGTAAAGCTTGGGGGTAGTTCTCTGACAGATAAGGAAGAGGCATCACTC
AGGCGTTTAGCTGAGCAGATTGCAGCATTAAAAGAGAGTGGCAATAAACTAGTGGTCGTG
CATGGAGGCGGCAGCTTCACTGATGGTCTGCTGGCATTGAAAAGTGGCCTGAGCTCGGGC
GAATTAGCTGCGGGGTTGAGGAGCACGTTAGAAGAGGCCGGAGAAGTAGCGACGAGGGAC
GCCCTAGCTAGCTTAGGGGAACGGCTTGTTGCAGCGCTGCTGGCGGCGGGTCTCCCTGCT
GTAGGACTCAGCGCCGCTGCGTTAGATGCGACGGAGGCGGGCCGGGATGAAGGCAGCGAC
GGGAACGTCGAGTCCGTGGACGCAGAAGCAATTGAGGAGTTGCTTGAGGCCGGGGTGGTC
CCCGTCCTAACAGGATTTATCGGCTTAGACGAAGAAGGGGAACTGGGAAGGGGATCTTCT
GACACCATCGCTGCGTTACTCGCTGAAGCTTTAGGCGCGGACAAACTCATAATACTGACC
GACGTAGACGGCGTTTACGATGCCGACCCTAAAAAGGTCCCAGACGCGAGGCTCTTGCCA
GAGATAAGTGTGGACGAGGCCGAGGAAAGCGCCTCCGAATTAGCGACCGGTGGGATGAAG
GTCAAACATCCAGCGGCTCTTGCTGCAGCTAGACGGGGGGGTATTCCGGTCGTGATAACG
AAT
>item3
CAGGGTCTGGATAACGCTAATCGTTCGCTAGTTCGCGCTACAAAAGCAGAAAGTTCAGAT
ATACGGAAAGAGGTGACTAACGGCATCGCTAAAGGGCTGAAGCTAGACAGTCTGGAAACA
GCTGCAGAGTCGAAGAACTGCTCAAGCGCACAGAAAGGCGGATCGCTAGCTTGGGCAACC
AACTCCCAACCACAGCCTCTCCGTGAAAGTAAGCTTGAGCCATTGGAAGACTCCCCACGT
AAGGCTTTAAAAACACCTGTGTTGCAAAAGACATCCAGTACCATAACTTTACAAGCAGTC
AAGGTTCAACCTGAACCCCGCGCTCCCGTCTCCGGGGCGCTGTCCCCGAGCGGGGAGGAA
CGCAAGCGCCCAGCTGCGTCTGCTCCCGCTACCTTACCGACACGACAGAGTGGTCTAGGT
TCTCAGGAAGTCGTTTCGAAGGTGGCGACTCGCAAAATTCCAATGGAGTCACAACGCGAG
TCGACT
"""
_desired_oamino = """>item1
PIISTLKESLTGDRITRIEGILNGTLNYILTEMEEEGASFSEALKEAQELGYAEADPTDD
VEGLDAARKLAILARLAFGLEVELEDVEVEGIEKLTAEDIEEAKEEGKVLKLVASAVEAR
VKPELVPKSHPLASVKGSDNAVAVETERVGELVVQGPGAGAEPTASAVLADLL
>item2
KRVVVKLGGSSLTDKEEASLRRLAEQIAALKESGNKLVVVHGGGSFTDGLLALKSGLSSG
ELAAGLRSTLEEAGEVATRDALASLGERLVAALLAAGLPAVGLSAAALDATEAGRDEGSD
GNVESVDAEAIEELLEAGVVPVLTGFIGLDEEGELGRGSSDTIAALLAEALGADKLIILT
DVDGVYDADPKKVPDARLLPEISVDEAEESASELATGGMKVKHPAALAAARRGGIPVVIT
N
>item3
QGLDNANRSLVRATKAESSDIRKEVTNGIAKGLKLDSLETAAESKNCSSAQKGGSLAWAT
NSQPQPLRESKLEPLEDSPRKALKTPVLQKTSSTITLQAVKVQPEPRAPVSGALSPSGEE
RKRPAASAPATLPTRQSGLGSQEVVSKVATRKIPMESQREST
"""

_consensus = """>Homoserine_dh-consensus
CCTATCATTTCGACGCTCAAGGAGTCGCTGACAGGTGACCGTATTACTCGAATCGAAGGG
ATATTAAACGGCACCCTGAATTACATTCTCACTGAGATGGAGGAAGAGGGGGCTTCATTC
TCTGAGGCGCTGAAGGAGGCACAGGAATTGGGCTACGCGGAAGCGGATCCTACGGACGAT
GTGGAAGGGCTAGATGCTGCTAGAAAGCTGGCAATTCTAGCCAGATTGGCATTTGGGTTA
GAGGTCGAGTTGGAGGACGTAGAGGTGGAAGGAATTGAAAAGCTGACTGCCGAAGATATT
GAAGAAGCGAAGGAAGAGGGTAAAGTTTTAAAACTAGTGGCAAGCGCCGTCGAAGCCAGG
GTCAAGCCTGAGCTGGTACCTAAGTCACATCCATTAGCCTCGGTAAAAGGCTCTGACAAC
GCCGTGGCTGTAGAAACGGAACGGGTAGGCGAACTCGTAGTGCAGGGACCAGGGGCTGGC
GCAGAGCCAACCGCATCCGCTGTACTCGCTGACCTTCTC
>AA_kinase-consensus
AAACGTGTAGTTGTAAAGCTTGGGGGTAGTTCTCTGACAGATAAGGAAGAGGCATCACTC
AGGCGTTTAGCTGAGCAGATTGCAGCATTAAAAGAGAGTGGCAATAAACTAGTGGTCGTG
CATGGAGGCGGCAGCTTCACTGATGGTCTGCTGGCATTGAAAAGTGGCCTGAGCTCGGGC
GAATTAGCTGCGGGGTTGAGGAGCACGTTAGAAGAGGCCGGAGAAGTAGCGACGAGGGAC
GCCCTAGCTAGCTTAGGGGAACGGCTTGTTGCAGCGCTGCTGGCGGCGGGTCTCCCTGCT
GTAGGACTCAGCGCCGCTGCGTTAGATGCGACGGAGGCGGGCCGGGATGAAGGCAGCGAC
GGGAACGTCGAGTCCGTGGACGCAGAAGCAATTGAGGAGTTGCTTGAGGCCGGGGTGGTC
CCCGTCCTAACAGGATTTATCGGCTTAGACGAAGAAGGGGAACTGGGAAGGGGATCTTCT
GACACCATCGCTGCGTTACTCGCTGAAGCTTTAGGCGCGGACAAACTCATAATACTGACC
GACGTAGACGGCGTTTACGATGCCGACCCTAAAAAGGTCCCAGACGCGAGGCTCTTGCCA
GAGATAAGTGTGGACGAGGCCGAGGAAAGCGCCTCCGAATTAGCGACCGGTGGGATGAAG
GTCAAACATCCAGCGGCTCTTGCTGCAGCTAGACGGGGGGGTATTCCGGTCGTGATAACG
AAT
>23ISL-consensus
CAGGGTCTGGATAACGCTAATCGTTCGCTAGTTCGCGCTACAAAAGCAGAAAGTTCAGAT
ATACGGAAAGAGGTGACTAACGGCATCGCTAAAGGGCTGAAGCTAGACAGTCTGGAAACA
GCTGCAGAGTCGAAGAACTGCTCAAGCGCACAGAAAGGCGGATCGCTAGCTTGGGCAACC
AACTCCCAACCACAGCCTCTCCGTGAAAGTAAGCTTGAGCCATTGGAAGACTCCCCACGT
AAGGCTTTAAAAACACCTGTGTTGCAAAAGACATCCAGTACCATAACTTTACAAGCAGTC
AAGGTTCAACCTGAACCCCGCGCTCCCGTCTCCGGGGCGCTGTCCCCGAGCGGGGAGGAA
CGCAAGCGCCCAGCTGCGTCTGCTCCCGCTACCTTACCGACACGACAGAGTGGTCTAGGT
TCTCAGGAAGTCGTTTCGAAGGTGGCGACTCGCAAAATTCCAATGGAGTCACAACGCGAG
TCGACT
"""


def test_cli_pscan3(tmp_path):
    os.chdir(tmp_path)
    invoke = CliRunner().invoke
    profile = example_filepath("minifam.hmm")
    with open("consensus.fasta", "w") as file:
        file.write(_consensus)

    with open("desired_output.gff", "w") as file:
        file.write(_desired_output)

    with open("desired_ocodon.fasta", "w") as file:
        file.write(_desired_ocodon)

    with open("desired_oamino.fasta", "w") as file:
        file.write(_desired_oamino)

    r = invoke(cli, ["pscan3", str(profile), "consensus.fasta"])
    assert r.exit_code == 0, r.output
    assert_same_file("oamino.fasta", "desired_oamino.fasta")
    assert_same_file("ocodon.fasta", "desired_ocodon.fasta")
    assert_same_file("output.gff", "desired_output.gff")
