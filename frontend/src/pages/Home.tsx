import SystemCard from "../components/SystemCard";
import { SystemStatus } from "../enums/SystemStatus";

export default function Home() {
  return (
    <div>
      <h1>
        SYSTEM MANAGER
      </h1>
      <SystemCard systemName="Test" systemStatus={SystemStatus.Offline}/>
    </div>
  )
}
