package Systems;
import javafx.beans.property.SimpleBooleanProperty;

/***
 * 
 * @author ProjectThetis
 *
 */
import com.pi4j.gpio.extension.pca.PCA9685GpioProvider;
import com.pi4j.gpio.extension.pca.PCA9685Pin;
import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinPwmOutput;
import com.pi4j.io.gpio.Pin;
import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CFactory;
public class InputSystem {
	
	protected SimpleBooleanProperty batteryLow; 
	protected SimpleBooleanProperty plasticFull;
	
	/**
	 * Default Constructor
	 */
	public InputSystem() {
		setupProperties();
	}
	
	private void setupProperties() {
		batteryLow = new SimpleBooleanProperty();
		plasticFull = new SimpleBooleanProperty();
	}
	
	/**
	 * Updates all read values, and sends log to file
	 * @return state of execution
	 */
	public boolean UpdateValues() {
		return false;
	}
	
}
