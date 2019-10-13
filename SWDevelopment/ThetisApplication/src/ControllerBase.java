import java.io.IOException;
import java.util.Dictionary;
import java.util.List;
import java.util.concurrent.TimeUnit;

/***
 * Controller provides basic functionality and interSystem communication
 * @author ProjectThetis
 * 
 */
public abstract class ControllerBase {
	protected Systems.DriveSystem driveSystem;
	protected Systems.InputSystem inputSystem;
	protected Systems.OpticalSystem opticalSystem;
	//protected Systems.SandSortingSystem SortingSystem;
	
	public String logFileName;
	
	private Thread driveThread;
	private DriveThread opticalThread;
	private InputThread inputThread;
	private SandSortingThread sandSortingThread;
	private List<Thread> Threads;

	public enum PropertyList{
		lowBattery,
		PlasticFull,
	}
	protected Dictionary<PropertyList,Object > PropertyDict;

	
	/**
	 * Default Controller Constructor
	 */
	public ControllerBase(){
		setupThreads();
		setupSystems();
	}
	
	private void setupThreads() {
		Threads.add(driveThread);
		Threads.add(inputThread);
		Threads.add(opticalThread);
		Threads.add(sandSortingThread);
	}
	
	private void setupSystems() {
		driveSystem = new Systems.DriveSystem();
		inputSystem = new Systems.InputSystem();
		opticalSystem = new Systems.OpticalSystem();
		PropertyDict.put(PropertyList.lowBattery, this.LowBatteryFunction());
		PropertyDict.put(PropertyList.PlasticFull,  this.PlasticFullFunction());
	}
	
	protected void startThreads() {
		for(Thread t : Threads) {
			t.run();
		}
	}
	
	protected boolean LowBatteryFunction() {
		return false;
	}
	protected boolean PlasticFullFunction() {
		return false;
	}
	
	/**
	 * Default function to start robot, producing required threads
	 *@return state of execution
	 */
	public boolean startBot() {
		return false;
	}
	
	/**
	 * Shuts all systems down
	 * @return state of execution
	 */
	public boolean emergencyStop() {
		return false;
	}
	
	/**
	 * Coordinates bot to return home
	 * @return state of execution
	 */
	public boolean returnHome() {
		return false;
	}
	
	/**
	 * Tests Drive motors
	 * @return state of execution
	 */
	public boolean testMotors() {
		return false;
	}
	
	/**
	 * Tests Vision systems
	 * @return state of execution
	 */
	protected boolean testOptical() {
		return false;
	}
}
