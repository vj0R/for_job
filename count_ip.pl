#!/usr/bin/perl

open(F1,"./file_ip");
$line = join('', <F1>);
@mass = $line=~m/((?:[0-9]{1,3}\.){3}(?:[0-9]{1,3}))/g;
map { $hash{$_} = undef } @mass;
print "\nnumber of elements in the array: ".scalar @mass."\n";
%hash_result;
while( ($k,$v) = each %hash ){
	$n = 0;
	for $i (@mass) {
		if ($i eq $k) {
			$n++;
		}
	}
	$hash_result{$k} = $n;
}
while( ($k,$v) = each %hash_result ){
	print "ip: ". $k ." count: ". $v ."\n";
}
