<?php
	$bool = 0;

	if (!($sql = ("SELECT `last_name`, `first_name`, `email`, `grade`, `id` FROM Students"))) {
		echo "Unable to generate query: Error 0x0005";
	}		

	$student_array = array();
	$count = 0;

	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			$ind_stu_array = array(); 
			$sln = $row["last_name"];
			$sfn = $row["first_name"];
			$sem = $row["email"];
			$sgr = $row["grade"];
			$sid = $row["id"];
			
			array_push($ind_stu_array, $sln);
			array_push($ind_stu_array, $sfn);
			array_push($ind_stu_array, $sid);
			array_push($ind_stu_array, $sem);
			array_push($ind_stu_array, $sgr);
			
			array_push($student_array, $ind_stu_array);
			$count++;
		}
	} else {
		echo "AHHHHH... Something went wrong!!";
	}

	for($i = $count-1; $i >= 0; $i--){
		echo '<script type="text/javascript">';
		$ln = $student_array[$i][0];
		$fn = $student_array[$i][1];
		$em = $student_array[$i][3];
		$id = $student_array[$i][2];
		$gr = $student_array[$i][4];
		echo "appendRowA('$ln','$fn','$id','$em','$gr');";
		echo '</script>';
	}

	$closest = 0;
	$closest_score = 0;
	$bool = 0;

	if($_POST) {
		$terms = $_POST['term'];
		for($i = 0; $i < $count; $i++){
			for($j = 0; $j < 4; $j++){
				$current = $student_array[$i][$j];
				//echo $current . " "; 
				$len = strlen($current);
				$len2 = strlen($terms);
				$score = 0;
				$done = 0;
				$rep = 0;
				$tmp_terms = substr($terms, $done, 1);
				for($k = 0; $k < $len; $k++){
					for($m = 0; $m < $len2; $m++){
						//echo strtolower($tmp_terms) . " vs. " . strtolower(substr($student_array[$i][$j], $k, 1)) . " ";
						if(strtolower(substr($student_array[$i][$j], $k, 1)) == strtolower($tmp_terms)){
							$score++;
							if($rep != 0){
								$score = $score + ($rep * 2);
							}
							$done++;
							$rep = 1;
							$tmp_terms = substr($terms, $done, 1);
							//echo "YEE HAW ";
							break;
						} else {
							$rep = 0;
							break;
						}
					}
				}
				//echo "..............." . $score;
				//echo "<br>";
				if($score > $closest_score){
					$closest = $i;
					$closest_score = $score;
				}
			}
		}
	}
	/* echo $closest . " ";
	echo $closest_score . " ";*/
	if($closest_score != 0){
		echo $student_array[$closest][1];
		echo " ";
		echo $student_array[$closest][0];
		echo " :: ";
		echo $student_array[$closest][2];
		echo " :: ";
		echo $student_array[$closest][3];
	}
?>
