import com.thinking.machines.hr.bl.pojo.*;
import com.thinking.machines.hr.bl.interfaces.pojo.*;
import com.thinking.machines.hr.bl.interfaces.pojo.*;
import com.thinking.machines.hr.bl.interfaces.managers.*;
import com.thinking.machines.hr.bl.managers.*;
import com.thinking.machines.hr.bl.exceptions.*;
import java.util.*;
class GetAllDesignationManager
{
public static void main(String gg[])
{
try
{
DesignationManagerInterface designationManager;
designationManager=DesignationManager.getDesignationManager();
Set<DesignationInterface> designations;
designations=new TreeSet<>();
designations=designationManager.getAll();
designations.forEach((designation)->{System.out.println("Code : "+designation.getCode()+"Title : "+designation.getTitle());});
}catch(BLException bl)
{
List<String>exceptions=bl.getPropertyExceptions();
exceptions.forEach((exception)->{System.out.println(exception);});
System.out.println(bl.getGenericException());
}
}

}