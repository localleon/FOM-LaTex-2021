# Call texcount perl-script for full output
perl tools/texcount.pl -merge thesis_main.tex 

echo ""
echo "thesis_main.tex contains: "
echo ""

# Call texcount script with short output 
perl tools/texcount.pl -merge -brief thesis_main.tex