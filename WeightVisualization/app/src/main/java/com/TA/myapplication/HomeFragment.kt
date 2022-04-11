package com.TA.myapplication

import android.graphics.Color
import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.lifecycle.ViewModelProvider
import com.TA.myapplication.data.Truck
import com.TA.myapplication.databinding.FragmentHomeBinding
import com.TA.myapplication.ui.HomeFragmentViewModel
import com.TA.myapplication.utility.AxisDateFormatter
import com.TA.myapplication.utility.ViewModelFactory
import com.github.mikephil.charting.components.Legend
import com.github.mikephil.charting.data.Entry
import com.github.mikephil.charting.data.LineDataSet
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ValueEventListener
import com.github.mikephil.charting.data.LineData

class HomeFragment : Fragment() {
    private var _binding : FragmentHomeBinding? = null
    private val binding get() = _binding!!

    private lateinit var factory : ViewModelFactory
    private lateinit var homeViewModel  : HomeFragmentViewModel

    private var dataPath : String = "data"

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        factory = ViewModelFactory.getInstance()
        homeViewModel = ViewModelProvider(this, factory)[HomeFragmentViewModel::class.java]
        val dataJson : DatabaseReference? = homeViewModel.getTheJson(dataPath)

        prepareChart(createDummyTrucks())

        Log.d(TAG, dataJson.toString())
        if (dataJson != null) {
            dataJson.addListenerForSingleValueEvent(object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    Log.d(TAG, snapshot.value.toString())
                }

                override fun onCancelled(error: DatabaseError) {
                    Log.d(TAG,"Error Here ${error.message.toString()}")
                }

            })
        }
        else {
            Log.d(TAG, "NO DATA !!")
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    fun createDummyTrucks() : ArrayList<Truck>{
        val trucks : ArrayList<Truck> = ArrayList()
        trucks.add(Truck("a",20.0,340.0))
        trucks.add(Truck("a",12.0,420.0))
        trucks.add(Truck("a",12.0,140.0))
        trucks.add(Truck("a",3.0,140.0))
        trucks.add(Truck("a",8.0,410.0))
        trucks.add(Truck("a",22.0,220.0))
        trucks.add(Truck("a",15.0,340.0))
        trucks.add(Truck("a",31.0,520.0))
        trucks.add(Truck("a",2.0,430.0))
        trucks.add(Truck("a",1.0,240.0))
        trucks.add(Truck("a",5.0,240.0))
        trucks.add(Truck("a",10.0,140.0))
        return trucks
    }

    private fun prepareChart(seriesData : ArrayList<Truck> ) {
        binding.linechart.setTouchEnabled(true)
        binding.linechart.setPinchZoom(true)
        val data = homeViewModel.prepareDummyData(seriesData)
        val dates = homeViewModel.dummyDates()
        val dataset : List<LineDataSet> = homeViewModel.makeDummyDataset(data)
        binding.linechart.xAxis.valueFormatter = AxisDateFormatter(dates.toArray(arrayOfNulls<String>(dates.size)))
        binding.linechart.data = LineData(dataset[0],dataset[1])
        val legend = binding.linechart.legend
        legend.isEnabled = true
        legend.verticalAlignment = Legend.LegendVerticalAlignment.TOP
        legend.horizontalAlignment = Legend.LegendHorizontalAlignment.CENTER

    }

    companion object {
        private val TAG :String = HomeFragment::class.java.simpleName
    }


}