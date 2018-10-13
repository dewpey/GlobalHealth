//
//  VaccinesTableViewController.swift
//  GlobalHealth
//
//  Created by Drew Patel on 10/13/18.
//  Copyright © 2018 Drew Patel. All rights reserved.
//

import UIKit
import Alamofire
import SwiftyJSON

class MasterViewControllerCell: UITableViewCell{

    @IBOutlet weak var nameLabel: UILabel!
}

class Vaccine {
    var name: String!
    var date: String!
    var location: String!
    init (value: NSDictionary) {
        name = value["name"] as? String
        date = value["date"] as? String
        location = value["location"] as? String
    }
}

class VaccinesTableViewController: UITableViewController {

    var vaccines = [Vaccine]()
    
    var blockchainHash = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()

        //loadData()
        loadMockData()
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem
    }

    // MARK: - Table view data source

    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return vaccines.count
    }

    func loadData(){

        let headers: HTTPHeaders = [
            "X-Username": "blurjoe@gmail.com",
            "X-Api-Key": "X0dvxIiNXXq5k7RBNYDmPrVoxEeJ+Y+umsUMS7FcgWk=",
            ]
        
        Alamofire.request("https://api.tierion.com/v1/records/cOsnFKqw1EKmYK3NMijTJg", method: .get, headers: headers).validate().responseJSON { response in
            switch response.result {
            case .success(let value):
                let json = JSON(value)
                self.blockchainHash = json["sha256"].string!
                let _vaccines = json["data"]["data"]
                print(_vaccines)
                print(self.blockchainHash)
            case .failure(let error):
                print(error)
            }
        }
        
    }
    
    func loadMockData(){
        let vaccine1: NSDictionary = [
            "name": "Hepatitis B",
            "time": "01/07/2013",
            "location": "Barnes Jewish Medical"
        ]
        let vaccine2: NSDictionary = [
            "name": "Diphtheria",
            "date": "03/07/2013",
            "location": "Barnes Jewish Medical"
        ]
        let vaccine3: NSDictionary = [
            "name": "Rotavirus vaccine",
            "date": "01/07/2013",
            "location": "St. Marys"
        ]
        self.vaccines.append(Vaccine(value: vaccine1))
        self.vaccines.append(Vaccine(value: vaccine2))
        self.vaccines.append(Vaccine(value: vaccine3))
        
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "vaccineCell", for: indexPath) as! MasterViewControllerCell

        let item = self.vaccines[indexPath.row]
        
        cell.nameLabel.text = item.name
        // Configure the cell...

        return cell
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
