import com.thinking.machines.hr.bl.pojo.*;
import com.thinking.machines.hr.bl.interfaces.pojo.*;
import com.thinking.machines.hr.bl.interfaces.pojo.*;
import com.thinking.machines.hr.bl.interfaces.managers.*;
import com.thinking.machines.hr.bl.managers.*;
import com.thinking.machines.hr.bl.exceptions.*;
import java.util.*;
class RemoveDesignationManager
{
public static void main(String gg[])
{
try
{
DesignationManagerInterface designationManager;
designationManager=DesignationManager.getDesignationManager();
Designation designation=new Designation();
designation.setCode(4);
designation.setTitle("kapil");
designationManager.remove(designation);
//System.out.println(designation.getCode());
}catch(BLException bl)
{
List<String>exceptions=bl.getPropertyExceptions();
exceptions.forEach((exception)->{System.out.println(exception);});
System.out.println(bl.getGenericException());
}
}

}