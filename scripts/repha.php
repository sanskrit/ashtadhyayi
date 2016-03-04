<?php
include 'dev-slp.php';
include 'slp-dev.php';
$filein = $argv[1];
$fout = fopen('rephalist.txt','a');
function rephacorrection($inputfile)
{
	global $fout;
	$data = file_get_contents($inputfile);
	$parts = explode('---',$data);
	$devadata = $parts[2];
	$slp1data = convert1($devadata);
	$devasplit = explode(' ',$devadata);
	$slp1split = explode(' ',$slp1data);
	/*
	$deva1data = convert($slp1data);
	$deva1split = explode(' ',$deva1data);
	print_r(array_diff($devasplit,$deva1split));
	*/
	foreach($slp1split as $value)
	{
		if (preg_match('/([aAiIuUfFxXeEoO])([kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh])r([kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]+[aAiIuUfFxXeEoO])/',$value))
		{
			$val1 = preg_replace('/([aAiIuUfFxXeEoO])([kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh])r([kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]+[aAiIuUfFxXeEoO])/','$1r$2$3',$value);
			fputs($fout,convert($value).":".convert($val1).":".$inputfile."\n");
		}
	}
}
rephacorrection($filein);
fclose($fout);
?>