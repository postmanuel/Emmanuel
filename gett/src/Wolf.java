import lombok.Data;



@Data
public class Wolf {
    public String name;
    public double weight;

    public Wolf(String name, double weight, int age) {
        this.name = name + " Acheampong";
        this.weight = weight + 7.0;
        this.age = age + 20;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public double getWeight() {
        return weight;
    }

    public int getAge() {
        return age;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int age;
}
