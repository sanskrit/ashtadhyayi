<?php
include '../../dev-slp.php';
include '../../slp-dev.php';
$filein = $argv[1];
$fout = fopen('issue10.txt','a');
function ten($inputfile)
{
	global $fout;
	$data = file_get_contents($inputfile);
	$parts = explode('---',$data);
	$devadata = $parts[2];
	$devasplit = explode(' ',$devadata);
	foreach($devasplit as $value)
	{
		if (preg_match('/[(][)]/',$value))
		{
			$value = trim($value);
			fputs($fout,$value.":".$value.":".$inputfile."\n");
		}
	}
}
ten($filein);
?>