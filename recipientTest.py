from OpenVaxxDB import recipient as ovr
from OpenVaxxDB import distributor as ovd
from OpenVaxxDB import business as ovb

testRecipient = ovr.recipient("CooperW824", "password0828", True)
testDistributor = ovd.distributor("Walgreens", "testPass", True)
testBusiness = ovb.business("Home Depot", "testPass1", True)

# recipient2 = ovr.recipient("CooperW8245", "1password0828")
# print(recipient2.get_user_data())
