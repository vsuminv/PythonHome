def output(student):
    print(f"{student['name']}\t{student['kor']}\t{student['eng']}\t{student['math']}",end='\t')
    print(f"{student['total']}\t{student['avg']:.2f}\t",end='\t')
    print(f"{student['grade']}")