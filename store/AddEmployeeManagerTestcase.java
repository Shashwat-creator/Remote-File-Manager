import com.thinking.machines.hr.bl.pojo.*;
import com.thinking.machines.hr.bl.interfaces.pojo.*;
import com.thinking.machines.hr.bl.interfaces.pojo.*;
import com.thinking.machines.hr.bl.interfaces.managers.*;
import com.thinking.machines.hr.bl.managers.*;
import com.thinking.machines.hr.bl.exceptions.*;
import com.thinking.machines.enums.*;
import java.util.*;
import java.math.*;
import java.text.*;
class AddEmployeeManager
{
public static void main(String gg[])
{
try
{
SimpleDateFormat sdf=new SimpleDateFormat("dd/MM/yyyy");
String name="Yash jain";
Date dateOfBirth=new Date();
String dateString="15/01/1901";
dateOfBirth=sdf.parse(dateString);
char gender='M';
String aadharCardNumber="012dc777";
String panNumber="66kfk23578";
int designationCode=Integer.parseInt("3");
BigDecimal basicSalary=new BigDecimal("450000");
boolean isIndian=true;
EmployeeManager employeeManager;
employeeManager=EmployeeManager.getEmployeeManager();
Employee employee=new Employee();
employee.setName(name);
employee.setDateOfBirth(dateOfBirth);
employee.setGender(GENDER.FEMALE);
employee.setAadharCardNumber(aadharCardNumber);
employee.setPANNumber(panNumber);
employee.setDesignationCode(designationCode);
employee.setBasicSalary(basicSalary);
employee.setisIndian(isIndian);
employeeManager.add(employee);
System.out.println(employee.getEmployeeId());
}catch(ParseException pe)
{
System.out.println(pe.getMessage());
}
catch(BLException bl)
{
List<String>exceptions=bl.getPropertyExceptions();
exceptions.forEach((exception)->{System.out.println(exception);});
System.out.println(bl.getGenericException());
}
}

}