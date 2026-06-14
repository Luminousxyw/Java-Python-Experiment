package com.expr2;
public class TestEmployee {
	public static void main(String[] args) {
		//无参数构造
		Employee emp1=new Employee();
		emp1.setID("E001");
		emp1.setNAME("张三");
		emp1.setDEPT("研发部");
		emp1.setSALARY(8000);
		emp1.showEmpInfo();
		//有参数构造
		Employee emp2=new Employee("E002","李四","财务部",7500);
		emp2.raiseSalary(500);
		emp2.showEmpInfo();
		//重写的toString
		System.out.println(emp1.toString());
		System.out.println(emp2);
		//重写equals
		System.out.println(emp1.equals(emp1));
		System.out.println(emp1.equals(emp2));
	}
}