package com.expr2;
public class Employee {
	private String id,name,dept;
	private double salary;
	public Employee() {
		
	}
	public Employee(String id,String name,String dept,double salary) {
		this.id=id;
		this.name=name;
		this.dept=dept;
		this.salary=salary;
	}
	public void showEmpInfo() {
		System.out.println("“编号："+id+"，姓名："+name+"，部门："+dept+"，薪资："+salary+"元”");
	}
	public void raiseSalary(double add) {
		this.salary+=add;
	}
	public void setId(String id) {
		this.id=id;
	}
	public void setName(String name) {
		this.name=name;
	}
	public void setDept(String dept) {
		this.dept=dept;
	}
	public void setSalary(double salary) {
		this.salary=salary;
	}
	public String getId() {
		return this.id;
	}
	public String getName() {
		return this.name;
	}
	public String getDept() {
		return this.dept;
	}
	public double getSalary() {
		return this.salary;
	}
	
	//toString equals
	
	public String toString() {
		return "Employee{编号：\""+id+"\"，姓名：\""+name+"\"，部门：\""+dept+"\"，薪资："+salary+"元}";
	}
	
	public boolean equals(Object obj) {
		if(this==obj) {
			return true;
		}
		else if(obj==null||getClass()!=obj.getClass()) {
			return false;
		}
		else {
			Employee other=(Employee) obj;
			return id!=null&&id.equals(other.id);
		}
	}
}
