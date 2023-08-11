#!/usr/bin/env perl

use warnings;

sub pprint {
  $seconds = shift;
  $h = int($seconds / 3600);
  $m = int($seconds / 60 % 60);
  $s = int($seconds % 60);
  if ($h > 0) {
    printf "%d:%02d:%02d", $h, $m, $s;
  } else {
    printf "%02d:%02d", $m, $s;
  }
}

$timer_file = '/tmp/badass_timer.tmp';
$now = `date +%s | tr -d '\\n'`;

sub get_state { split ' ', `cat $timer_file` }
sub set_state { 
  my $start = shift;
  my $pause = shift // "0";
  `echo -n "$start $pause" > $timer_file`;
}

$arg = shift @ARGV // "help";
for ($arg) {
  if (/^start/) { 
    if (-e $timer_file) {
      my ($start, $pause) = get_state();
      exit if $pause eq '0';
      $next_start = ($now - $pause) + $start;
      set_state($next_start);
      print "Timer resumed.\n";
    } else {
      set_state($now);
      print "Timer started.\n";
    }
  }
  elsif (/^pause/) {
    exit unless -e $timer_file;
    my ($start, $pause) = get_state();
    set_state($start, $now);
    print "Timer paused.\n";
  }
  elsif (/^show/) {
    exit unless -e $timer_file;
    my ($start, $pause) = get_state();
    $show = $pause eq '0' ? ($now - $start) : ($pause - $start);
    pprint($show)
  }
  elsif (/^stop/) { 
    `rm $timer_file`;
    print "Timer stopped.\n";
  }
  else { 
    print "???\n";
  }
}
