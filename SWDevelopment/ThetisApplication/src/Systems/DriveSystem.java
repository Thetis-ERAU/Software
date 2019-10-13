package Systems;

/***
 * 
 * @author ProjectThetis
 *
 *library from https://pi4j.com/1.2/download.html
 */
import com.pi4j.gpio.extension.pca.PCA9685GpioProvider;
import com.pi4j.gpio.extension.pca.PCA9685Pin;
import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinPwmOutput;
import com.pi4j.io.gpio.Pin;
import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CFactory;

public class DriveSystem {

	public DriveSystem() {

	}

	/**
	 * Turns the Robot relative to the angleRad, changing the speed to speed
	 * 
	 * @param angleRad describes desired turn, pos is CCW
	 * @param speed    describes set speed of motors in m/s
	 * @return state of execution
	 */
	public boolean TurnBot(double angleRad, double speed) {

		return false;
	}

	/**
	 * Changes the overall speed of the bot
	 * 
	 * @param speed describes set speed of motors in m/s
	 * @return state of execution
	 */
	public boolean ChangeSpeed(double speed) {
		return false;
	}
	/**
	 * Stops all drive functions of the bot immediately
	 * @return state of execution
	 */
	public boolean Stop() {
		return false;
	}

	/**
	 * Testing method that fires right motor for ___ time
	 * 
	 * @return state of execution
	 */
	public boolean FireRightMotor() {
		return false;
	}

	/**
	 * Testing method that fires left motor for ___ time
	 * 
	 * @return state of execution
	 */
	public boolean FireLeftMotor() {
		return false;
	}

}
