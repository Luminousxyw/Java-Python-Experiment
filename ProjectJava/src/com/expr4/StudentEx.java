package com.expr4;

public class StudentEx extends Person implements Award {
    private double score;
    private String className;

    public StudentEx(String name, int age, double score, String className) {
        super(name, age);
        this.score = score;
        this.className = className;
    }

    public double getScore() {
        return score;
    }

    public String getClassName() {
        return className;
    }

    @Override
    public void showInfo() {
        System.out.println("Name: " + name + ", Age: " + age + ", Score: " + score + ", Class: " + className);
    }

    @Override
    public String getAward() {
        if (score >= 90) {
            return name + " wins an award (score " + score + " >= 90)";
        }
        return name + " does not qualify for award";
    }

    @Override
    public String toString() {
        return "StudentEx{name='" + name + "', age=" + age + ", score=" + score + ", class='" + className + "'}";
    }
}