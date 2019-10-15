import java.io.IOException;
import java.util.*;

/***
 * Controller provides basic functionality and interSystem communication
 * @author ProjectThetis
 * 
 */
public abstract class ControllerBase extends ThreadBase{
	
	public String logFileName;
	
	private DriveThread driveThread;
	private OpticalThread opticalThread;
	private InputThread inputThread;
	private SandSortingThread sandSortingThread;
	private List<Thread> Threads;

	public enum PropertyList{
		lowBattery,
		PlasticFull,
	}
	protected HashMap<PropertyList,Object > PropertyDict;//"Dictionary"

	
	/**
	 * Default Controller Constructor
	 */
	public ControllerBase(){
		setupThreads();
		setupSystems();
	}
	
	private void setupThreads() {
		driveThread = new DriveThread();
		opticalThread = new OpticalThread();
		inputThread = new InputThread();
		sandSortingThread = new SandSortingThread();
		Threads = new ArrayList<Thread>();
		Threads.add(driveThread);
		Threads.add(inputThread);
		Threads.add(opticalThread);
		Threads.add(sandSortingThread);
	}
	
	private void setupSystems() {
		PropertyDict = new HashMap<PropertyList, Object>();
		PropertyDict.put(PropertyList.lowBattery, this.LowBatteryFunction());
		PropertyDict.put(PropertyList.PlasticFull,  this.PlasticFullFunction());
	}
	/**
	 * Starts all threads in Threads(private)
	 */
	protected void startThreads() {
		for(Thread t : Threads) {
			t.run();
		}
	}
	
	/**
	 * Executed when low battery property flips
	 * @return state of execution
	 */
	protected boolean LowBatteryFunction() {
		return false;
	}
	
	/**
	 * Executed when Plastic full Property flips
	 * @return state of execution
	 */
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
