import React from "react";
import '../styles/routineSurvey.css'

const RoutineSurvey = () => {
    return (
        <div className="routine-survey">
            <form className="routine-survey-form">
                <div className="survey-header-container">
                    <h2>Sustainability Survey</h2>
                </div>

                <div class="question">
                    <h3>What best describes your commute to work?</h3>
                    <div>
                    <input type="radio" id="commute-drive-alone" name="commute" value="drive-alone"/>
                    <label for="commute-drive-alone">I drive alone</label>
                    </div>
                    <div>
                    <input type="radio" id="commute-alt-transport" name="commute" value="alt-transport"/>
                    <label for="commute-alt-transport">I use alternative transportation (carpool, public transit, bike, walk)</label>
                    </div>
                    <div>
                    <input type="radio" id="commute-work-from-home" name="commute" value="work-from-home"/>
                    <label for="commute-work-from-home">I work from home</label>
                    </div>
                    <div>
                    <input type="radio" id="commute-not-applicable" name="commute" value="not-applicable"/>
                    <label for="commute-not-applicable">Not applicable</label>
                    </div>
                </div>

                <div class="question">
                    <h3>How often do you typically purchase new clothing?</h3>
                    <div>
                    <input type="radio" id="clothing-more-monthly" name="clothing" value="more-monthly"/>
                    <label for="clothing-more-monthly">More than once a month</label>
                    </div>
                    <div>
                    <input type="radio" id="clothing-monthly" name="clothing" value="monthly"/>
                    <label for="clothing-monthly">About once a month</label>
                    </div>
                    <div>
                    <input type="radio" id="clothing-less-monthly" name="clothing" value="less-monthly"/>
                    <label for="clothing-less-monthly">Less than once a month</label>
                    </div>
                </div>

                <div class="question">
                    <h3>Are you often home for the majority of the weekend?</h3>
                    <div>
                    <input type="radio" id="weekend-home" name="weekend" value="yes"/>
                    <label for="weekend-home">Yes</label>
                    </div>
                    <div>
                    <input type="radio" id="weekend-not-home" name="weekend" value="no"/>
                    <label for="weekend-not-home">No</label>
                    </div>
                </div>

                <div class="question">
                    <h3>In a typical week, how often do you use plastic utensils at least once throughout the day?</h3>
                    <div>
                    <input type="radio" id="plastic-utensils-never" name="plastic-utensils" value="never"/>
                    <label for="plastic-utensils-never">Never</label>
                    </div>
                    <div>
                    <input type="radio" id="plastic-utensils-1-3" name="plastic-utensils" value="1-3"/>
                    <label for="plastic-utensils-1-3">1-3</label>
                    </div>
                    <div>
                    <input type="radio" id="plastic-utensils-4-7" name="plastic-utensils" value="4-7"/>
                    <label for="plastic-utensils-4-7">4-7</label>
                    </div>
                </div>

                <div class="question">
                    <h3>On average, how often do you use and discard single-use food containers?</h3>
                    <div>
                    <input type="radio" id="disposable-containers-never" name="disposable-containers" value="never"/>
                    <label for="disposable-containers-never">Never</label>
                    </div>
                    <div>
                    <input type="radio" id="disposable-containers-1-3" name="disposable-containers" value="1-3"/>
                    <label for="disposable-containers-1-3">1-3</label>
                    </div>
                    <div>
                    <input type="radio" id="disposable-containers-4-7" name="disposable-containers" value="4-7"/>
                    <label for="disposable-containers-4-7">4-7</label>
                    </div>
                </div>

                <div class="question">
                    <h3>Do you bring reusable bags with you when shopping?</h3>
                    <div>
                    <input type="radio" id="reusable-bags-yes" name="reusable-bags" value="yes"/>
                    <label for="reusable-bags-yes">Yes</label>
                    </div>
                    <div>
                    <input type="radio" id="reusable-bags-no" name="reusable-bags" value="no"/>
                    <label for="reusable-bags-no">No</label>
                    </div>
                    <div>
                    <input type="radio" id="reusable-bags-sometimes" name="reusable-bags" value="sometimes"/>
                    <label for="reusable-bags-sometimes">Sometimes</label>
                    </div>
                </div>

                <div class="question">
                    <h3>How often do you tend to purchase coffee to-go?</h3>
                    <div>
                    <input type="radio" id="coffee-to-go-never" name="coffee-to-go" value="never"/>
                    <label for="coffee-to-go-never">Never</label>
                    </div>
                    <div>
                    <input type="radio" id="coffee-to-go-1-3" name="coffee-to-go" value="1-3"/>
                    <label for="coffee-to-go-1-3">1-3 times a week</label>
                    </div>
                    <div>
                    <input type="radio" id="coffee-to-go-4-7" name="coffee-to-go" value="4-7"/>
                    <label for="coffee-to-go-4-7">4-7 times a week</label>
                    </div>
                </div>

                <div className="button-container">
                  <button className='submit' type="submit">Submit</button>
                </div>
            </form>
        </div>
    )
}

export default RoutineSurvey;