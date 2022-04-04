package com.TA.myapplication.ui

import android.graphics.Color
import android.util.Log
import androidx.lifecycle.ViewModel
import com.TA.myapplication.HomeFragment
import com.TA.myapplication.data.Truck
import com.TA.myapplication.repository.DataRepository
import com.github.mikephil.charting.data.Entry
import com.github.mikephil.charting.data.LineDataSet
import com.google.firebase.database.DatabaseReference

class HomeFragmentViewModel(private val dataRepository : DataRepository) : ViewModel(){

    fun getTheJson(path : String ) : DatabaseReference?{
        return dataRepository.getJsonFromDatabase(path)
    }

    fun getTruckInformation(){
    }

    fun prepareDummyData(list_weights : List<Truck>) : List<ArrayList<Entry>> {
        val currentTruckMin = ArrayList<Entry>()
        val currentTruckMax = ArrayList<Entry>()

        Log.d(TAG, list_weights.toString())
        for (i in 0 .. list_weights.size - 1) {
            currentTruckMin.add(Entry(i.toFloat(),list_weights[i].standard_weight.toFloat()))
            currentTruckMax.add(Entry(i.toFloat(),list_weights[i].full_weight.toFloat()))
        }
        return listOf(currentTruckMin,currentTruckMax)
    }


     fun dummyDates() : ArrayList<String> {
        val date = ArrayList<String>()
        date.add("01-Apr")
        date.add("02-Apr")
        date.add("03-Apr")
        date.add("04-Apr")
        date.add("05-Apr")
        date.add("06-Apr")
        date.add("07-Apr")
        date.add("08-Apr")
        date.add("09-Apr")
        date.add("10-Apr")

        return date
    }
    private fun prepareDataset(dataset : LineDataSet,type : String ="min") : LineDataSet{
        dataset.mode = LineDataSet.Mode.CUBIC_BEZIER
        dataset.circleRadius = 5f
        if (type == "min") {
            dataset.color = Color.BLUE

            dataset.setCircleColor(Color.BLUE)
        }
        else if (type=="max") {
            dataset.color = Color.RED
            dataset.setCircleColor(Color.RED)
        }
        return dataset
    }

    fun makeDummyDataset(listData : List<ArrayList<Entry>>) : List<LineDataSet> {
        val minData = listData[0]
        val maxData = listData[1]
        var minDataset = LineDataSet(minData , "Minimum")
        var maxDataset = LineDataSet(maxData , "Minimum")
        minDataset = prepareDataset(minDataset,"min")
        maxDataset = prepareDataset(maxDataset,"max")
        return listOf(minDataset,maxDataset)
    }


    companion object {
        val TAG : String = HomeFragment::class.java.simpleName
    }
}